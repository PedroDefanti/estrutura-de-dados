#EXERCICIO 2

def conta_marica(texto):
    palavra_escolhida='Maricá'
    if palavra_escolhida not in texto:
        return 0
    else:
        tamanho_palavra=len(palavra_escolhida)
        encontrar_palavra=texto.find(palavra_escolhida)
        resto_frase=texto[tamanho_palavra+encontrar_palavra:]
        return 1+ conta_marica(resto_frase)

frase="Maricá é linda. Maricá tem lagoas."
verificar=conta_marica(frase)
print(f'A palavra (Maricá) aparece {verificar} vezes')