#EXERCICIO 4

def fatorial(n):
    if n<=1:
        return 1
    else:
        return n* fatorial(n-1)
numero=5
fatoracao=fatorial(numero)
print(f'O fatorial de {numero} é {fatoracao}')