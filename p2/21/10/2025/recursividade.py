#EXERCICIO 1

# def lista(lista):
#     if len(lista)==1:
#         return lista[0]
#     else:
#        return lista[0]+lista(lista[1:])
# ingresos=[6,15,3,5,9]

# soma_ingressos=lista(ingresos)

# print(f'A soma dos ingressos vendidos pelos quiosques da orla de Itaipuaçu foi de {soma_ingressos} ')

#EXERCICIO 2

# def conta_marica(texto):
#     palavra_escolhida='Maricá'
#     if palavra_escolhida not in texto:
#         return 0
#     else:
#         tamanho_palavra=len(palavra_escolhida)
#         encontrar_palavra=texto.find(palavra_escolhida)
#         resto_frase=texto[tamanho_palavra+encontrar_palavra:]
#         return 1+ conta_marica(resto_frase)

# frase="Maricá é linda. Maricá tem lagoas."
# verificar=conta_marica(frase)
# print(f'A palavra (Maricá) aparece {verificar} vezes')

#EXERCICIO 3

# def reverter(s):
#     if s=='':
#         return ''
#     else:
#         return s[-1]+reverter(s[:-1])
# palavra="Itaipuaçu"
# palavra_inversa=reverter(palavra)
# print(f'o inverso de {palavra} é {palavra_inversa}')

#EXERCICIO 4

# def fatorial(n):
#     if n<=1:
#         return 1
#     else:
#         return n* fatorial(n-1)
# numero=5
# fatoracao=fatorial(numero)
# print(f'O fatorial de {numero} é {fatoracao}')

#EXERCICIO 5

# def maximo(lista):
#     if len(lista) == 1:
#         return lista[0]
#     else:
#         primeiro_elemento = lista[0]
#         maximo_do_resto = maximo(lista[1:])

#         if primeiro_elemento > maximo_do_resto:
#             return primeiro_elemento
#         else:
#             return maximo_do_resto

# notas = [7.5, 8.2, 9.0, 8.8]
# resultado = maximo(notas)

# print(f"Lista de Notas: {notas}")
# print(f"A maior nota em Ponta Negra é: {resultado}")

#EXERCICIOS 6
# def aplica_desconto(lista, d):
#     fator_desconto = 1 - (d / 100)
#     if not lista:
#         return []
#     else:

#         primeiro = lista[0]
#         resto_da_lista = lista[1:]
#         novo_primeiro = primeiro * fator_desconto
#         return [novo_primeiro] + aplica_desconto(resto_da_lista, d)

# precos = [10, 20, 50, 15]
# desconto = 10
# resultado = aplica_desconto(precos, desconto)

# print(f"Preços Originais: {precos}")
# print(f"Desconto Aplicado: {desconto}%")
# print(f"Preços com Desconto: {resultado}") 

