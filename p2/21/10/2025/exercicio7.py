def conta_pares(lista):
    if not lista: 
        return 0
    else:
        primeiro = lista[0]
        resto_da_lista = lista[1:]

        if primeiro % 2 == 0:
            return 1 + conta_pares(resto_da_lista)
        else:
            return 0 + conta_pares(resto_da_lista)


medicoes = [2, 3, 4, 7, 8, 10, 1]
resultado = conta_pares(medicoes)

print(f"Lista de Medições: {medicoes}")
print(f"Total de números pares: {resultado}") 