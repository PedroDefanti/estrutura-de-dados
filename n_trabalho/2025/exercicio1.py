# EXERCICIO 1

def soma(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma(lista[1:])
ingressos=[1,2,3,4,5]

soma_ingressos=soma(ingressos)

print(f'A soma dos ingressos vendidos pelos quiosques da orla de Itaipuaçu foi de {soma_ingressos} ')