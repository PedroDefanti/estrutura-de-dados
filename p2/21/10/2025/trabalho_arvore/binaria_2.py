class Node:
    def __init__(self,valor):
        self.valor=valor
        self.esquerda=None
        self.direita=None
        
    def __repr__(self):
        return f"Node({self.valor})"
    
class BinarySearchTree:
    def __init__(self):
        
        self.raiz=None
    
    def insert(self,valor):
        self.raiz=self.insert_recursive(self.raiz,valor)
    
    def insert_recursive(self,no_atual,valor):
        
        if no_atual is None:
            return Node(valor)
        
        if valor < no_atual.valor:
            no_atual.esquerda=self.insert_recursive(no_atual.esquerda,valor)
        
        elif valor>no_atual.valor:
            no_atual.direita=self.insert_recursive(no_atual.direita,valor)
        
        return no_atual
    
    def search(self,valor):
        
        return self.search_recursive(self.raiz,valor)
    
    def search_recursive(self,no_atual,valor):
        
        if no_atual is None:
            return False
        
        if no_atual.valor==valor:
            return True
        
        if valor<no_atual.valor:
            return self.search_recursive(no_atual.esquerda,valor)
        
        else:
            return self.search_recursive(no_atual.direita,valor)

    