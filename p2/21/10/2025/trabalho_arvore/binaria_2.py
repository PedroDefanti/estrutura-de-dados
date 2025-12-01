import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        
    def __repr__(self):
        return f"Node({self.valor})"
    
class BinarySearchTree:
    def __init__(self):
        self.raiz = None
    
    def insert(self, valor):
        self.raiz = self.insert_recursive(self.raiz, valor)
    
    def insert_recursive(self, no_atual, valor):
        if no_atual is None:
            return Node(valor)
        
        if valor < no_atual.valor:
            no_atual.esquerda = self.insert_recursive(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            no_atual.direita = self.insert_recursive(no_atual.direita, valor)
        
        return no_atual
    
    def search(self, valor):
        return self.search_recursive(self.raiz, valor)
    
    def search_recursive(self, no_atual, valor):
        if no_atual is None:
            return False
        
        if no_atual.valor == valor:
            return True
        
        if valor < no_atual.valor:
            return self.search_recursive(no_atual.esquerda, valor)
        else:
            return self.search_recursive(no_atual.direita, valor)
        
    def in_order(self):
        resultado = []
        self.in_order_recursive(self.raiz, resultado)
        return resultado
        
    def in_order_recursive(self, no_atual, resultado):
        if no_atual is None:
            return
        
        self.in_order_recursive(no_atual.esquerda, resultado)
        resultado.append(no_atual.valor)
        self.in_order_recursive(no_atual.direita, resultado)
    
    def delete(self, valor):
        """Deleta um valor e rebalanceia automaticamente a árvore"""
        self.raiz = self.delete_recursive(self.raiz, valor)
        # Rebalanceamento automático após exclusão
        self.balancear()
        
    def delete_recursive(self, no_atual, valor):
        if no_atual is None:
            return no_atual 
        
        if valor < no_atual.valor:
            no_atual.esquerda = self.delete_recursive(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            no_atual.direita = self.delete_recursive(no_atual.direita, valor)
        else:
            if no_atual.esquerda is None and no_atual.direita is None:
                return None
                
            if no_atual.esquerda is None:
                return no_atual.direita
            
            if no_atual.direita is None:
                return no_atual.esquerda
            
            sucessor = self.find_min_node(no_atual.direita)
            no_atual.valor = sucessor.valor
            no_atual.direita = self.delete_recursive(no_atual.direita, sucessor.valor)
        
        return no_atual
    
    def find_min_node(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual
    
    def balancear(self):
        """Rebalanceia a árvore coletando todos os valores e reconstruindo"""
        valores = self.in_order()
        self.raiz = self.construir_balanceada(valores, 0, len(valores) - 1)
    
    def construir_balanceada(self, valores, inicio, fim):
        """Constrói uma árvore balanceada a partir de uma lista ordenada"""
        if inicio > fim:
            return None
        
        meio = (inicio + fim) // 2
        no = Node(valores[meio])
        
        no.esquerda = self.construir_balanceada(valores, inicio, meio - 1)
        no.direita = self.construir_balanceada(valores, meio + 1, fim)
        
        return no


def construir_grafo(no_atual, grafo):
    if no_atual is not None:
        grafo.add_node(no_atual.valor)
        
        if no_atual.esquerda:
            grafo.add_node(no_atual.esquerda.valor)
            grafo.add_edge(no_atual.valor, no_atual.esquerda.valor)
            construir_grafo(no_atual.esquerda, grafo)
            
        if no_atual.direita:
            grafo.add_node(no_atual.direita.valor)
            grafo.add_edge(no_atual.valor, no_atual.direita.valor)
            construir_grafo(no_atual.direita, grafo)


def calcular_posicoes_hierarquicas(no_atual, pos, x=0, y=0, largura=4):
    """Calcula as posições dos nós de forma hierárquica"""
    if no_atual is None:
        return
    
    pos[no_atual.valor] = (x, y)
    
    if no_atual.esquerda or no_atual.direita:
        nova_largura = largura / 2
        
        if no_atual.esquerda:
            calcular_posicoes_hierarquicas(
                no_atual.esquerda, pos, 
                x - nova_largura, y - 1, nova_largura
            )
        
        if no_atual.direita:
            calcular_posicoes_hierarquicas(
                no_atual.direita, pos, 
                x + nova_largura, y - 1, nova_largura
            )


def visualizar_arvore(bst, titulo="Visualização da Árvore Binária de Busca (BST)"):
    """Visualiza a árvore binária"""
    if bst.raiz is None:
        print("⚠ A árvore está vazia!")
        return
    
    G = nx.DiGraph()
    construir_grafo(bst.raiz, G)
    
    pos = {}
    calcular_posicoes_hierarquicas(bst.raiz, pos)
    
    try:
        from networkx.drawing.nx_pydot import graphviz_layout
        pos = graphviz_layout(G, prog='dot')
    except:
        pass
    
    plt.figure(figsize=(12, 8))
    plt.title(titulo, fontsize=16, fontweight='bold')
    
    nx.draw(
        G,
        pos,
        with_labels=True, 
        node_size=1500, 
        node_color='lightblue',
        font_size=12, 
        font_weight='bold', 
        arrows=True, 
        arrowstyle='->', 
        arrowsize=20,
        edge_color='gray',
        linewidths=2,
        edgecolors='darkblue'
    )
    
    plt.tight_layout()
    plt.show()


def menu_principal():
    """Menu interativo para manipular a BST"""
    print("=" * 50)
    print("  ÁRVORE BINÁRIA DE BUSCA (BST) - INTERATIVA")
    print("=" * 50)
    
    # Entrada de valores iniciais
    print("\n📝 Digite os valores iniciais da árvore (separados por espaço):")
    print("   Exemplo: 50 30 70 20 40 60 80")
    entrada = input(">>> ")
    
    valores = []
    try:
        valores = [int(x.strip()) for x in entrada.split() if x.strip()]
    except ValueError:
        print("⚠ Valores inválidos! Usando valores padrão: [50, 30, 70, 20, 40, 60, 80]")
        valores = [50, 30, 70, 20, 40, 60, 80]
    
    if not valores:
        print("⚠ Nenhum valor digitado! Usando valores padrão: [50, 30, 70, 20, 40, 60, 80]")
        valores = [50, 30, 70, 20, 40, 60, 80]
    
    # Criar e popular a BST
    bst = BinarySearchTree()
    print(f"\n✓ Inserindo valores: {valores}")
    for v in valores:
        bst.insert(v)
    
    print(f"✓ Árvore em ordem: {bst.in_order()}")
    visualizar_arvore(bst, "Árvore Inicial")
    
    # Loop do menu
    while True:
        print("\n" + "=" * 50)
        print("  MENU DE OPERAÇÕES")
        print("=" * 50)
        print("1. 📥 Incluir elemento")
        print("2. 🗑️  Excluir elemento (rebalanceamento automático)")
        print("3. 🔍 Procurar elemento")
        print("4. 📊 Visualizar árvore")
        print("5. 📋 Mostrar elementos em ordem")
        print("6. ⚖️  Rebalancear árvore manualmente")
        print("0. 🚪 Sair")
        print("=" * 50)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            # Incluir elemento
            try:
                valor = int(input("\n📥 Digite o valor a incluir: "))
                if bst.search(valor):
                    print(f"⚠ O valor {valor} já existe na árvore!")
                else:
                    bst.insert(valor)
                    print(f"✓ Valor {valor} incluído com sucesso!")
                    print(f"✓ Árvore em ordem: {bst.in_order()}")
                    visualizar_arvore(bst, f"Após incluir {valor}")
            except ValueError:
                print("⚠ Valor inválido!")
        
        elif opcao == "2":
            # Excluir elemento com rebalanceamento automático
            try:
                valor = int(input("\n🗑️  Digite o valor a excluir: "))
                if not bst.search(valor):
                    print(f"⚠ O valor {valor} não existe na árvore!")
                else:
                    bst.delete(valor)
                    print(f"✓ Valor {valor} excluído e árvore rebalanceada automaticamente!")
                    print(f"✓ Árvore em ordem: {bst.in_order()}")
                    visualizar_arvore(bst, f"Após excluir {valor} (rebalanceada)")
            except ValueError:
                print("⚠ Valor inválido!")
        
        elif opcao == "3":
            # Procurar elemento
            try:
                valor = int(input("\n🔍 Digite o valor a procurar: "))
                if bst.search(valor):
                    print(f"✓ O valor {valor} FOI ENCONTRADO na árvore!")
                else:
                    print(f"✗ O valor {valor} NÃO FOI ENCONTRADO na árvore!")
            except ValueError:
                print("⚠ Valor inválido!")
        
        elif opcao == "4":
            # Visualizar árvore
            print("\n📊 Gerando visualização...")
            visualizar_arvore(bst)
        
        elif opcao == "5":
            # Mostrar elementos em ordem
            valores_ordenados = bst.in_order()
            if valores_ordenados:
                print(f"\n📋 Elementos em ordem: {valores_ordenados}")
            else:
                print("\n⚠ A árvore está vazia!")
        
        elif opcao == "6":
            # Rebalancear manualmente
            bst.balancear()
            print("\n✓ Árvore rebalanceada manualmente!")
            print(f"✓ Árvore em ordem: {bst.in_order()}")
            visualizar_arvore(bst, "Árvore Rebalanceada Manualmente")
        
        elif opcao == "0":
            print("\n👋 Encerrando programa. Até logo!")
            break
        
        else:
            print("\n⚠ Opção inválida! Tente novamente.")


# Executar o programa
if __name__ == "__main__":
    menu_principal()