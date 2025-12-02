# pip install networkx matplotlib

import matplotlib.pyplot as plt
import networkx as nx

# --- Grafo direcionado ---
G = nx.DiGraph()

# Vértices (turmas)
nodes = ['7A', '6B', '7B', '6A', '8A', '8B']
G.add_nodes_from(nodes)

pos = {
    "7A": (0.25, 0.80),
    "6B": (0.85, 0.80),
    "7B": (0.10, 0.40),
    "6A": (0.90, 0.40),
    "8A": (0.35, 0.10),
    "8B": (0.75, 0.10),
}

# Arestas (direções como na com setas)
edges = [
 ('6A', '7A'),   
 ('6A', '7B'),
 ('6A', '8B'),
 ('6B', '7A'),
 ('6B', '8A'),
 ('6B', '8B'),
 ('7A', '6A'),
 ('7A', '6B'),
 ('7B', '6A'),
 ('7B', '8A'),
 ('7B', '8B'),
 ('8A', '6B'),
 ('8A', '7B'),
 ('8B', '6A'),
 ('8B', '7B'),
 ('8A', '8B'),

]
G.add_edges_from(edges)

# --- Desenho ---
fig, ax = plt.subplots(figsize=(9, 6))
ax.set_aspect('equal')

# Nós
nx.draw_networkx_nodes(
    G, pos, node_color='#A7D0E8', edgecolors='k',
    node_size=2200, linewidths=1.8, ax=ax
)
nx.draw_networkx_labels(G, pos, font_size=14, font_weight='bold', ax=ax)

# Arestas com setas visíveis
nx.draw_networkx_edges(
    G, pos, edgelist=edges, ax=ax,
    arrows=True,                 
    arrowstyle='-|>',           
    arrowsize=28,               
    width=2.2, edge_color='black',
    connectionstyle='arc3,rad=0',
    min_source_margin=18,       
    min_target_margin=18        
)

plt.title('Introdução à Teoria de Grafos: Estrutura de Dados', pad=12)
plt.axis('off')
plt.tight_layout()
plt.show()
