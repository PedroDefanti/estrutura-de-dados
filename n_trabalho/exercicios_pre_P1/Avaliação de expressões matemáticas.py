'''
Desenvolva um programa
que utilize duas pilhas para avaliar expressões matemáticas em
notação pós-fixa (notação polonesa reversa). Por exemplo, a
expressão 3 4 + 2 * 7 / deve ser avaliada corretamente como 2.
'''

'''
expressao='2+2'
l=[]
for i in expressao
se o i for um  numero and len de l ==1:
    retirar=l.pop()
    x=int(i)
    eu adiciono=l.append(x)

se o i for um  numero:
    x=int(i)
    eu adiciono=l.append(x)
se o i for um  numero and len de l ==1:


'''

expressao = '3 4 + 2 * 7 /'.split()
pilha=[]

for i in expressao:
    if i.isdigit():
        pilha.append(i)
    else:
        operador=i
        if len(pilha)<3:
            print('ERRO!!!!')
        n1=pilha.pop()
        n2=pilha.pop()

        conta=f'{n2} {operador} {n1}'
        resultado=eval(conta)

        pilha.append(resultado)
        print(pilha)
        
       