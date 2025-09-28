'''
Crie um programa em Python que use uma
pilha para inverter a ordem dos dígitos de um número inteiro. Por
exemplo, o número 1234 deve ser invertido para 4321.
'''

lista=[]

while True:
    numero=int(input('Digite o número a ser adicionado:'))
    if numero==0:
        break
    else:
        lista.append(numero)
n=lista.copy()
inverso=[]
for i in range(len(lista)):
    remover=lista.pop()
    inverso.append(remover)

print(f'O conjunto de números {n} virou {inverso}')
