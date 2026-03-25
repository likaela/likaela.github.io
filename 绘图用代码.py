import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

nodes = ["A公司", "B公司", "C公司", "D公司", "E公司", "F公司", "G公司"]
node_profit = {"A公司":80, "B公司":-60, "C公司":30, "D公司":-90, "E公司":50, "F公司":90, "G公司":30}
edges = [
    ("A公司", "B公司", {"correlation":0.8}), ("A公司", "C公司", {"correlation":0.3}),
    ("B公司", "C公司", {"correlation":0.9}), ("C公司", "E公司", {"correlation":0.5}),
    ("D公司", "E公司", {"correlation":0.3}), ("C公司", "D公司", {"correlation":0.5}),
    ("E公司", "A公司", {"correlation":0.8}), ("F公司", "A公司", {"correlation":0.5}),
    ("G公司", "B公司", {"correlation":0.4}), ("F公司", "G公司", {"correlation":0.6}),
    ("G公司", "B公司", {"correlation":0.8}), ("B公司", "F公司", {"correlation":0.7}),
    ("C公司", "G公司", {"correlation":0.7})
]

G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

node_colors = []
for node in G.nodes():
    profit = node_profit[node]
    if profit > 0:
        node_colors.append((1, 0.4, 0.4, abs(profit)/100))
    else:
        node_colors.append((0.4, 1, 0.4, abs(profit)/100))
edge_widths = [d["correlation"] * 10 for (u, v, d) in G.edges(data=True)]
edge_curvatures = [d["correlation"] * 0.2 for (u, v, d) in G.edges(data=True)]

plt.figure(figsize=(10, 8), facecolor="#f5f5f5")
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
pos = nx.spring_layout(G, seed=42, k=0.3)

nx.draw_networkx_nodes(
    G, pos,
    node_color=node_colors,
    node_size=1500,
    edgecolors="white",
    linewidths=2
)

for i, (u, v, d) in enumerate(G.edges(data=True)):
    nx.draw_networkx_edges(
        G, pos,
        edgelist=[(u, v)],
        width=edge_widths[i],
        edge_color="#666666",
        alpha=0.8,
        arrows=True,
        connectionstyle=f"arc3,rad={edge_curvatures[i]}",
        arrowstyle='->',
        arrowsize=15
    )
    mid_x = (pos[u][0] + pos[v][0]) / 2
    mid_y = (pos[u][1] + pos[v][1]) / 2
    dx = pos[v][0] - pos[u][0]
    dy = pos[v][1] - pos[u][1]
    angle = np.arctan2(dy, dx)
    offset = 0.05
    label_x = mid_x + offset * np.sin(angle)
    label_y = mid_y - offset * np.cos(angle)
    plt.text(
        label_x, label_y,
        f"{d['correlation']:.1f}",
        ha='center', va='center',
        fontsize=9,
        bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="gray", lw=0.5)
    )

nx.draw_networkx_labels(
    G, pos,
    font_size=11,
    font_weight="bold",
    font_color="white"
)

plt.axis("off")
plt.title("金融关联网络", fontsize=13, pad=15)
plt.tight_layout()
plt.show()
