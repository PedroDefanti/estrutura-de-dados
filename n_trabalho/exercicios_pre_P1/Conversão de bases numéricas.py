'''Desenvolva um programa que use
uma pilha para converter um número da base decimal para uma
base binária. O usuário deve inserir um número em base decimal e o
programa deve retornar sua representação em binário.'''

n=789
lista=[]
divisor=2

while True:
    resto=n%divisor
    
    div=n//divisor
    if n==1:
        resto=1%divisor
        lista.append(resto)
        break
    else:
        if n%2==1:
            n=n-(div+1)
        else:
            n=n//2
        lista.append(resto)
    
    

    
inversao=[]
for i in  range(len(lista)):
    retirar=lista.pop()
    inversao.append(retirar)
print(inversao)
