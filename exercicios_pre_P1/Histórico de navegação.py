''' Crie um programa que simule o histórico de
navegação de um navegador usando pilha. O programa deve permitir
ao usuário "visitar" páginas web, voltar para a página anterior e
mostrar o histórico atual.'''
lista=[]
while True:
    pagina=input('Digite a página que desja visitar:')
    if pagina=='n':
        break
    else:
        lista.append(pagina)
print(lista)