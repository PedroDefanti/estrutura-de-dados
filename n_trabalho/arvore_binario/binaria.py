def ler_arquivo_txt():
    nome_arquivo = 'numeros.txt'
    lista_de_numeros = []
    
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                linha_limpa = linha.strip()

                if linha_limpa:
                    try:
                        numero = int(linha_limpa)
                        lista_de_numeros.append(numero)
                    except ValueError:

                        print(f" Aviso: Ignorando linha '{linha_limpa}'. Não é um número inteiro válido.")
                        
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        
    return lista_de_numeros

lista_n = ler_arquivo_txt()
lista_n.sort()

lista_n=ler_arquivo_txt()
lista_n.sort()

def busca_binaria_fatiamento_recursiva(lista, n, indice_base=0):

    if not lista:
        return f' O número {n} não está na lista.'
        
    meio_local = len(lista) // 2
    if meio_local >= len(lista):
        return f'O número {n} não está na lista.'

    if lista[meio_local] == n:
        indice_original = indice_base + meio_local
        return f'Número encontrado no índice {indice_original}'
    elif n > lista[meio_local]:
        nova_lista = lista[meio_local + 1:]
        novo_indice_base = indice_base + meio_local + 1
        return busca_binaria_fatiamento_recursiva(nova_lista, n, novo_indice_base)

    else:
        nova_lista = lista[:meio_local]
        return busca_binaria_fatiamento_recursiva(nova_lista, n, indice_base)





resultado_existente = busca_binaria_fatiamento_recursiva(lista_n, 70)
print(f"Buscando 70: {resultado_existente}")





