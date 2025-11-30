from collections import deque
class Node:
    def __init__(self,valor):
        self.valor=valor
        self.esquerda=None
        self.direita=None

class BinaryTree:
    def __init__(self,valor_raiz=None):
        if valor_raiz is not None:
            self.raiz=Node(valor_raiz)
        else:
            self.raiz=None
    
    def pre_order(self):
        print('Pré-order(Recursivo)')
        self.pre_order_recursive(self.raiz)
    
    def pre_order_recursive(self,no_atual):
        if no_atual is None:
            return
        print(f'{no_atual.valor}',end="")
        
        self.pre_order_recursive(no_atual.esquerda)
        
        self.pre_order_recursive(no_atual.direita)
        
    
    def pre_order_iterative(self):
        print('Pré-order(Iterativo):')
        if self.raiz is None:
            return
        
        pilha=[]
        pilha.append(self.raiz)        
        while pilha:
            no_atual=pilha.pop()
            
            print(f'{no_atual.valor}',end="-")
            
            if no_atual.direita:
                pilha.append(no_atual.direita)
                
                
            if no_atual.esquerda:
                pilha.append(no_atual.esquerda)
    
    
    def in_order(self):
        print('In-order (Recursivo)')
        self.in_order_recursive(self.raiz)
        print()
    
    def in_order_recursive(self,no_atual):
        if no_atual is None:
            return
        self.in_order_recursive(no_atual.esquerda)
        
        print(f'{no_atual.valor}',end='')
        
        self.in_order_recursive(no_atual.direita)
    
    def in_order_iterative(self):
        print("In-order (Iterativo)")
        pilha=[]
        no_atual=self.raiz
        
        while True:
            if no_atual is not None:
                pilha.append(no_atual)
                no_atual=no_atual.esquerda
            elif pilha:
                no_atual=pilha.pop()
                
                print(f'{no_atual.valor}',end="-")
                
                no_atual=no_atual.direita
            else:
                break
        print()
        
    def post_order(self):
        print('Post-order (Recursivo)')
        self.post_order_recursive(self.raiz)
        
        
    def post_order_recursive(self,no_atual):
        if no_atual is None:
            return
        self.post_order_recursive(no_atual.esquerda)
        
        self.post_order_recursive(no_atual.direita)
        
        print(f'{no_atual.valor}',end="-")
        
    
    def post_order_iterative(self):
        print('Post-order (Iterativo):')
        if self.raiz is None:
            return
        pilha1=[self.raiz]
        pilha2=[]
        
        while pilha1:
            no_atual=pilha1.pop()
            pilha2.append(no_atual)
            
            if no_atual.esquerda:
                pilha1.append(no_atual.esquerda)
                
            if no_atual.direita:
                pilha1.append(no_atual.direita)
                
        while pilha2:
            no=pilha2.pop()
            
            print(f'{no.valor}',end="-")
            
        print()
        
        
    def level_order(self):
        print('Level-order (BFS):')
        if self.raiz is None:
            return
        
        fila=deque()
        fila.append(self.raiz)
        
        while fila:
            no_atual=fila.popleft()
            
            print(f'{no_atual.valor}',end="-")
            
            
            if no_atual.esquerda:
                fila.append(no_atual.esquerda)
                
                
            if no_atual.direita:
                fila.append(no_atual.direita)
        print()

# Construir a árvore manualmente
arvore = BinaryTree(1)
arvore.raiz.esquerda = Node(2)
arvore.raiz.direita = Node(3)
arvore.raiz.esquerda.esquerda = Node(4)
arvore.raiz.esquerda.direita = Node(5)
arvore.raiz.direita.esquerda = Node(6)
print("--- Testando Travessias na Árvore ---")
# (Raiz, Esq, Dir)
arvore.pre_order()
arvore.pre_order_iterative()
# (Esq, Raiz, Dir)
arvore.in_order()
arvore.in_order_iterative()
# (Esq, Dir, Raiz)
arvore.post_order()
arvore.post_order_iterative()
# (Nível por Nível)
arvore.level_order()

                