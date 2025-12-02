'''Escreva um código que use uma pilha
para verificar se os parênteses em uma expressão matemática estão
corretamente balanceados. A entrada será uma string contendo
parênteses, colchetes e chaves, e o programa deve retornar se a
sequência é válida ou não.'''


lista=[]

expressao='(5+9[78+2])'

for i in expressao:
    if '(' in i:
        lista.append(i)
    elif ')' in i:
        lista.pop()
if len(lista)==0:
    print('Expresaao valida')
else:
    print('INVALIDA')
    print(lista)