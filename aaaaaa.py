cidades = []
quantidade_de_cidades=int(input('Digite a quantidade que deseja adicionar:'))

for i in range(quantidade_de_cidades):
    cidade=input(f'Digite o nome da cidade{i+1}:')
    cidades.append(cidade)
print(cidades)

estradas = []

pares_tratados = set() 


for c1 in cidades:
    for c2 in cidades:
        # Pular se for a mesma cidade
        if c1 == c2:
            continue
        
        if (c2, c1) in pares_tratados:
            continue
        pares_tratados.add((c1, c2))
        
        relacao_c1_c2 = input(f'Deseja criar uma estrada DE {c1} PARA {c2} (s/n): ').lower().strip()
        
        if relacao_c1_c2 == 's':
            while True:
                try:
                    peso_c1_c2 = int(input(f'Digite o peso  para {c1} -> {c2}: '))
                    if peso_c1_c2 <= 0:
                        print("O peso deve ser um valor positivo.")
                        continue
                    estradas.append((c1, c2, peso_c1_c2))
                    break
                except ValueError:
                    print("Entrada inválida. Digite um número inteiro positivo para o peso.")
                    
            relacao_c2_c1 = input(f'Deseja criar também a estrada DE {c2} PARA {c1} (Retorno) (s/n): ').lower().strip()
            
            if relacao_c2_c1 == 's':
                while True:
                    try:
                        peso_c2_c1 = int(input(f'Digite o peso (custo/tempo) para {c2} -> {c1}: '))
                        if peso_c2_c1 <= 0:
                            print("O peso deve ser um valor positivo.")
                            continue
                        estradas.append((c2, c1, peso_c2_c1))
                        break
                    except ValueError:
                        print("Entrada inválida. Digite um número inteiro positivo para o peso.")

print(f'\nEstradas coletadas: {estradas}')


pos={}


for i in cidades:
    x=int(input(f'Digite a posição x da cidade {i}:'))
    y=int(input(f'Digite a posição x da cidade {i}:'))
    posicoes=x,y
    pos[i]=posicoes
print(pos)
