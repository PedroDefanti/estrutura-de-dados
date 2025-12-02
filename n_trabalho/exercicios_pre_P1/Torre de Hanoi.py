'''Implemente o problema da Torre de Hanoi usando
pilhas em Python. O programa deve ser capaz de resolver o
problema para n discos e exibir os movimentos necessários para
mover todos os discos da torre inicial para a torre destino.'''


def torre_de_hanoi_iterativa(n_discos):
    # 1. Definição das Torres (Pilhas)
    # A torre A (Origem) começa com todos os discos (do maior ao menor)
    torre_a = list(range(n_discos, 0, -1)) # [n, n-1, ..., 1]
    torre_b = [] # Auxiliar
    torre_c = [] # Destino
    
    torres = {'A': torre_a, 'B': torre_b, 'C': torre_c}
    
    # 2. Definição da Pilha de Controle para Simular a Recursão
    # Cada item da pilha será uma tarefa (discos a mover, origem, destino, auxiliar)
    pilha_controle = []
    
    # 3. Definição das Torres de Trabalho (Baseado na Paridade de N)
    # O algoritmo iterativo inverte as torres B e C se N for par.
    if n_discos % 2 == 0:
        origem, destino, auxiliar = 'A', 'C', 'B'
    else:
        origem, destino, auxiliar = 'A', 'B', 'C'
        
    movimentos = []

    # Passo Inicial: Coloca a tarefa principal na pilha de controle
    pilha_controle.append((n_discos, origem, destino, auxiliar))

    # --- LOOP PRINCIPAL ---
    
    # 4. Processamento das Tarefas
    while pilha_controle:
        # Pega a próxima subtarefa da pilha (POP)
        n, origem, destino, auxiliar = pilha_controle.pop()

        if n == 1:
            # CASO BASE: Se for apenas 1 disco, mova-o diretamente.
            disco = torres[origem].pop()
            torres[destino].append(disco)
            movimentos.append(f"Mova o disco {disco} de {origem} para {destino}")
        
        elif n > 1:
            # PASSO RECURSIVO SIMULADO (Divide a tarefa em 3 partes, empilhadas na ordem inversa)
            
            # 3º: Mover n-1 discos da Auxiliar para o Destino
            # (Esta tarefa será a primeira a ser processada quando desempilhada)
            pilha_controle.append((n - 1, auxiliar, destino, origem))

            # 2º: Mover o maior disco (n) da Origem para o Destino
            pilha_controle.append((1, origem, destino, auxiliar))

            # 1º: Mover n-1 discos da Origem para a Auxiliar
            # (Esta tarefa será a última a ser processada nesta rodada)
            pilha_controle.append((n - 1, origem, auxiliar, destino))
    print(torre_c)

    return movimentos

# --- Execução ---

N = 3  # Número de discos
movimentos_necessarios = torre_de_hanoi_iterativa(N)

print(f"--- Torre de Hanói para N = {N} Discos ---")
for i, movimento in enumerate(movimentos_necessarios, 1):
    print(f"{i}. {movimento}")

print(f"\nTotal de movimentos: {len(movimentos_necessarios)}")

print(movimentos_necessarios,)