#EXERCICIO 5

def maximo(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        primeiro_elemento = lista[0]
        maximo_do_resto = maximo(lista[1:])

        if primeiro_elemento > maximo_do_resto:
            return primeiro_elemento
        else:
            return maximo_do_resto

notas = [7.5, 8.2, 9.0, 8.8]
resultado = maximo(notas)

print(f"Lista de Notas: {notas}")
# print(f"A maior nota em Ponta Negra é: {resultado}")