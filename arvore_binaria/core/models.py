# core/models.py
from django.db import models
import json
import math

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class BinarySearchTree:
    def __init__(self):
        self.raiz = None
    
    # ----------------------------------------------------
    # OPERAÇÕES BÁSICAS (CRUD)
    # ----------------------------------------------------

    def insert(self, valor):
        """Insere um valor na árvore mantendo a propriedade BST."""
        self.raiz = self.insert_recursive(self.raiz, valor)
    
    def insert_recursive(self, no_atual, valor):
        """Lógica recursiva para inserção de um nó."""
        if no_atual is None:
            return Node(valor)
        
        # Ignora valores duplicados (comportamento comum de BST)
        if valor < no_atual.valor:
            no_atual.esquerda = self.insert_recursive(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            no_atual.direita = self.insert_recursive(no_atual.direita, valor)
        
        return no_atual

    def search(self, valor):
        """Busca um valor na árvore. Retorna True ou False."""
        return self._search_recursive(self.raiz, valor)
    
    def _search_recursive(self, no_atual, valor):
        if no_atual is None:
            return False
        
        if no_atual.valor == valor:
            return True
        
        if valor < no_atual.valor:
            return self._search_recursive(no_atual.esquerda, valor)
        else:
            return self._search_recursive(no_atual.direita, valor)

    def _find_min(self, no):
        """Encontra o nó com o menor valor em uma subárvore."""
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def delete(self, valor):
        """Remove um valor da árvore. Retorna True se deletado, False se não encontrado."""
        found_before = self.search(valor)
        self.raiz = self._delete_recursive(self.raiz, valor)
        return found_before and not self.search(valor)

    def _delete_recursive(self, no_atual, valor):
        """Lógica recursiva para a deleção de um nó."""
        if no_atual is None:
            return no_atual

        if valor < no_atual.valor:
            no_atual.esquerda = self._delete_recursive(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            no_atual.direita = self._delete_recursive(no_atual.direita, valor)
        else:
            # Nó com apenas um filho ou sem filhos
            if no_atual.esquerda is None:
                return no_atual.direita
            elif no_atual.direita is None:
                return no_atual.esquerda
            
            # Nó com dois filhos: pega o sucessor in-order (menor da subárvore direita)
            temp = self._find_min(no_atual.direita)
            no_atual.valor = temp.valor
            
            # Deleta o sucessor in-order
            no_atual.direita = self._delete_recursive(no_atual.direita, temp.valor)

        return no_atual
    
    # ----------------------------------------------------
    # OPERAÇÃO DE BALANCEAMENTO (DSW) - Implementação Robusta
    # ----------------------------------------------------

    def _right_rotate(self, pai):
        """Rotaciona um nó para a direita, retornando o novo topo da subárvore."""
        filho = pai.esquerda
        pai.esquerda = filho.direita
        filho.direita = pai
        return filho

    def _left_rotate(self, pai):
        """Rotaciona um nó para a esquerda, retornando o novo topo da subárvore."""
        filho = pai.direita
        pai.direita = filho.esquerda
        filho.esquerda = pai
        return filho
    
    # DSW - Principal função de balanceamento
    def balance(self):
        """Balanceia a árvore usando o algoritmo DSW (Day-Stout-Warren)."""
        if self.raiz is None:
            return

        # 1. Cria a espinha (Vine)
        dummy_root = Node(None) 
        dummy_root.direita = self.raiz
        atual = dummy_root
        
        while atual.direita:
            if atual.direita.esquerda:
                # Rotaciona para a direita
                atual.direita = self._right_rotate(atual.direita)
            else:
                # Move para o próximo nó da espinha
                atual = atual.direita
        
        self.raiz = dummy_root.direita 

        # 2. Calcula o número de nós (n) e o tamanho da maior subárvore completa (m)
        n = len(self.in_order())
        
        # k = altura da maior subárvore completa (2^k - 1 <= n)
        k = int(math.log2(n + 1))
        # m = número de nós dessa subárvore (2^k - 1)
        m = (2 ** k) - 1

        # 3. Rotações iniciais para criar a maior subárvore completa
        rotacoes_iniciais = n - m
        atual = dummy_root
        for _ in range(rotacoes_iniciais):
            # Rotações à esquerda
            atual.direita = self._left_rotate(atual.direita)
            atual = atual.direita
        
        # 4. Rotações em loops decrescentes (m/2, m/4, ...)
        m = m // 2
        while m > 0:
            atual = dummy_root
            for _ in range(m):
                atual.direita = self._left_rotate(atual.direita)
                atual = atual.direita
                
            m = m // 2
                
        self.raiz = dummy_root.direita
                
    # ----------------------------------------------------
    # Traversal (Percurso) e Conversão de Dados
    # ----------------------------------------------------

    def in_order(self):
        """Retorna uma lista de valores em ordem (crescente)."""
        return self._in_order_recursive(self.raiz, [])

    def _in_order_recursive(self, no, result):
        if no:
            self._in_order_recursive(no.esquerda, result)
            result.append(no.valor)
            self._in_order_recursive(no.direita, result)
        return result

    def to_dict(self):
        """Converte a árvore em um dicionário para serialização (JSON/Front-end)."""
        if self.raiz is None:
            return None
        return self._node_to_dict(self.raiz)
    
    def _node_to_dict(self, no):
        """Método auxiliar para converter um nó em dicionário"""
        if no is None:
            return None
        
        return {
            'valor': no.valor,
            'esquerda': self._node_to_dict(no.esquerda),
            'direita': self._node_to_dict(no.direita)
        }
    
    def from_dict(self, data):
        """Reconstrói a árvore a partir de um dicionário."""
        if data is None:
            return None
        
        no = Node(data['valor'])
        # Garante que acessa usando .get para lidar com None
        no.esquerda = self.from_dict(data.get('esquerda'))
        no.direita = self.from_dict(data.get('direita'))
        
        return no

# ----------------------------------------------------
# MODELO DJANGO PARA PERSISTÊNCIA
# ----------------------------------------------------

class BSTSession(models.Model):
    session_key = models.CharField(max_length=100, unique=True)
    tree_data = models.TextField(default='null')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_tree(self):
        """Retorna a árvore BST a partir dos dados persistidos."""
        bst = BinarySearchTree()
        if self.tree_data and self.tree_data != 'null':
            try:
                data = json.loads(self.tree_data)
                # Garante que a raiz seja None se os dados estiverem vazios
                bst.raiz = bst.from_dict(data) if data else None
            except (json.JSONDecodeError, KeyError):
                bst.raiz = None
        return bst
    
    def set_tree(self, bst):
        """Salva o estado atual da árvore BST."""
        self.tree_data = json.dumps(bst.to_dict()) if bst.raiz else 'null'
        self.save()