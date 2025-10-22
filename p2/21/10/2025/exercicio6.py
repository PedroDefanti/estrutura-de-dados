#EXERCICIOS 6
def aplica_desconto(lista, d):
    fator_desconto = 1 - (d / 100)
    if not lista:
        return []
    else:

        primeiro = lista[0]
        resto_da_lista = lista[1:]
        novo_primeiro = primeiro * fator_desconto
        return [novo_primeiro] + aplica_desconto(resto_da_lista, d)

precos = [10, 20, 50, 15]
desconto = 10
resultado = aplica_desconto(precos, desconto)

print(f"Preços Originais: {precos}")
print(f"Desconto Aplicado: {desconto}%")
print(f"Preços com Desconto: {resultado}") 