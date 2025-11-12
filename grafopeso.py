from math import radians
import matplotlib.pyplot as plt
import networkx as nx

# =========================
# FUNÇÕES DE UTILIDADE
# =========================

def desenhar_grafo(grafo, pos, titulo, caminho_destaque=None):
    """Desenha o grafo, opcionalmente destacando um caminho."""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_aspect('equal')
    
    # Desenhar Nós e Rótulos
    nx.draw_networkx_nodes(grafo, pos, node_color='#A7D0E8', edgecolors='k',
                            node_size=1800, linewidths=1.8, ax=ax)
    nx.draw_networkx_labels(grafo, pos, font_size=12, font_weight='bold', ax=ax)
    
    # Desenhar Arestas (Padrão)
    nx.draw_networkx_edges(grafo, pos, arrows=True, arrowstyle='-|>', arrowsize=24,
                            width=2, edge_color='black', ax=ax)

    # Destacar o caminho (se fornecido)
    if caminho_destaque:
        caminho_arestas = list(zip(caminho_destaque[:-1], caminho_destaque[1:]))
        nx.draw_networkx_edges(grafo, pos, edgelist=caminho_arestas, 
                                edge_color='red', width=3, arrows=True,
                                arrowstyle='-|>', arrowsize=24, ax=ax)
    
    # Rótulos de pesos
    edge_labels = {(u, v): d['weight'] for u, v, d in grafo.edges(data=True)}
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=edge_labels, font_size=11, ax=ax)
    
    plt.title(titulo, pad=10)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

# =========================
# PARTE 1 — REPRESENTAÇÃO (DINÂMICA)
# =========================

print("--- 🗺️ Configuração da Rede de Cidades ---")

# 1) Define as cidades
cidades = []
while True:
    try:
        quantidade_de_cidades = int(input('Digite a quantidade de cidades/pontos (mínimo 3): '))
        if quantidade_de_cidades < 3:
            print("Por favor, digite um número maior ou igual a 3.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        
for i in range(quantidade_de_cidades):
    cidade = input(f'Digite o nome da Cidade/Ponto {i+1}: ').strip()
    cidades.append(cidade)

print(f'\nCidades adicionadas: {cidades}')

# 2) Cria o grafo direcionado
G = nx.DiGraph()
G.add_nodes_from(cidades)

# 3) Estradas (arestas) com custos
estradas = []
pares_tratados = set() 

print("\n--- 🛣️ Definição das Estradas e Custos ---")
for c1 in cidades:
    for c2 in cidades:
        
        if c1 == c2:
            continue
        
        # Pular se o par (c2, c1) já foi tratado para evitar repetição do prompt
        if (c2, c1) in pares_tratados:
            continue
        pares_tratados.add((c1, c2))
        
        # Criação c1 -> c2
        relacao_c1_c2 = input(f'Deseja criar uma estrada DE {c1} PARA {c2} (s/n): ').lower().strip()
        
        if relacao_c1_c2 == 's':
            while True:
                try:
                    peso_c1_c2 = int(input(f'Digite o peso para {c1} -> {c2}: '))
                    if peso_c1_c2 <= 0:
                        print("O peso deve ser um valor positivo.")
                        continue
                    estradas.append((c1, c2, peso_c1_c2))
                    break
                except ValueError:
                    print("Entrada inválida. Digite um número inteiro positivo para o peso.")
                    
            # Criação c2 -> c1 (Retorno Opcional)
            relacao_c2_c1 = input(f'Deseja criar também a estrada DE {c2} PARA {c1} (Retorno) (s/n): ').lower().strip()
            
            if relacao_c2_c1 == 's':
                while True:
                    try:
                        peso_c2_c1 = int(input(f'Digite o peso para {c2} -> {c1}: '))
                        if peso_c2_c1 <= 0:
                            print("O peso deve ser um valor positivo.")
                            continue
                        estradas.append((c2, c1, peso_c2_c1))
                        break
                    except ValueError:
                        print("Entrada inválida. Digite um número inteiro positivo para o peso.")

G.add_weighted_edges_from(estradas)

# 4) Posição dos nós para visualização (CORRIGIDO: Usando NetworkX layout automático)
# Usaremos o layout 'spring' para uma visualização automática baseada nas conexões
pos = nx.spring_layout(G, seed=42)

# 5) Desenhar o grafo inicial
desenhar_grafo(G, pos, 'Rede de Cidades (Custos nas estradas)')

# =========================
# PARTE 2 — CAMINHO MÍNIMO (AUTOMÁTICO - DIJKSTRA)
# =========================

print("\n--- 🎯 Definição de Origem e Destino ---")
while True:
    origem = input(f'Digite a cidade de ORIGEM (de {cidades}): ').strip()
    destino = input(f'Digite a cidade de DESTINO (de {cidades}): ').strip()
    
    if origem not in cidades or destino not in cidades:
        print("Origem ou destino inválidos. Escolha entre as cidades listadas.")
    elif origem == destino:
        print("Origem e destino devem ser diferentes.")
    else:
        break

print("\n--- 🤖 Cálculo do Caminho Mínimo (Dijkstra) ---")

try:
    # 1. Encontrar o caminho de menor custo
    melhor_rota_inicial = nx.shortest_path(G, source=origem, target=destino, weight='weight')
    melhor_custo_inicial = nx.shortest_path_length(G, source=origem, target=destino, weight='weight')
    
    print('\nMENOR CAMINHO INICIAL:')
    print(f'Rota: {melhor_rota_inicial} | Custo total: {melhor_custo_inicial}')
    
    # Desenhar o grafo destacando o caminho mínimo
    desenhar_grafo(G, pos, f'Caminho Mínimo: {origem} -> {destino}', caminho_destaque=melhor_rota_inicial)
    
except nx.NetworkXNoPath:
    melhor_rota_inicial = None
    melhor_custo_inicial = None
    print(f'❌ Não existe caminho válido de {origem} para {destino} na rede inicial.')


# =========================
# PARTE 3 — FALHA (Simulação Dinâmica)
# =========================

print("\n--- ⚠️ Simulação de Falha na Rede ---")
falha = None
while True:
    falha_origem = input('Digite a ORIGEM da estrada que deve falhar (ou digite "n" para ignorar a falha): ').strip()
    if falha_origem.lower() == 'n':
        break
        
    falha_destino = input(f'Digite o DESTINO da estrada que falhou (de {falha_origem}): ').strip()
    falha = (falha_origem, falha_destino)

    if G.has_edge(*falha):
        G.remove_edge(*falha)
        print(f'\n[AVISO] Falha simulada: estrada removida {falha_origem} -> {falha_destino}')
        break
    else:
        print(f'\n[INFO] Estrada {falha_origem} -> {falha_destino} não existia ou o nome estava incorreto. Tente novamente ou digite "n".')


# =========================
# PARTE 4 — REANÁLISE E ROBUSTEZ
# =========================

if falha:
    # Desenhar o grafo após a falha
    desenhar_grafo(G, pos, 'Rede de Cidades após falha')

    print("\n--- 🔄 Recálculo do Caminho Mínimo Após Falha ---")
    
    try:
        melhor_rota_apos_falha = nx.shortest_path(G, source=origem, target=destino, weight='weight')
        melhor_custo_apos_falha = nx.shortest_path_length(G, source=origem, target=destino, weight='weight')

        print('\nMENOR CAMINHO APÓS FALHA:')
        print(f'Rota: {melhor_rota_apos_falha} | Custo total: {melhor_custo_apos_falha}')
        
        # Desenhar o grafo destacando o novo caminho mínimo
        desenhar_grafo(G, pos, f'Novo Caminho Mínimo Após Falha: {origem} -> {destino}', caminho_destaque=melhor_rota_apos_falha)
        
        # Análise de Robustez
        print('\n[ANÁLISE DE ROBUSTEZ]')
        if melhor_custo_inicial is None:
             print('O caminho original já não existia. A falha não alterou a conectividade para essa rota.')
        elif melhor_custo_apos_falha == melhor_custo_inicial:
            print('✅ **ROBUSTO**: A falha não afetou o custo do caminho mínimo.')
        elif melhor_custo_apos_falha > melhor_custo_inicial:
            print(f'⚠️ **PARCIALMENTE ROBUSTO**: O custo aumentou de {melhor_custo_inicial} para {melhor_custo_apos_falha}.')
            print(f'A rota anterior ({melhor_rota_inicial}) foi afetada.')
        
    except nx.NetworkXNoPath:
        print(f'❌ **NÃO ROBUSTO**: Não restou nenhum caminho válido de {origem} para {destino} após a falha da estrada {falha}.')
        print('A estrada removida era **crítica** para esta rota.')
else:
    print('\nNenhuma falha simulada. Análise de robustez finalizada.')