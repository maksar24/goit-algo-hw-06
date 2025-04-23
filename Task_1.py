import networkx as nx
import matplotlib.pyplot as plt


connections = [
    ("Bond Street", "Oxford Circus"),
    ("Bond Street", "Green Park"),
    ("Oxford Circus", "Green Park"),  
    ("Green Park", "Piccadilly Circus"),
    ("Piccadilly Circus", "Oxford Circus"),
    ("Piccadilly Circus", "Leicester Square"),
    ("Oxford Circus", "Tottenham Court Road"),
    ("Leicester Square", "Tottenham Court Road"),
    ("Leicester Square", "Covent Garden"),
    ("Covent Garden", "Holborn"),
    ("Holborn", "Tottenham Court Road"),
]

G = nx.Graph()
G.add_edges_from(connections)

plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=2000,
        font_size=10, font_weight='bold', edge_color='gray')
plt.title("London Underground — Central Area", fontsize=14)
plt.show()

# Analyze the graph
print("Number of stations (nodes):", G.number_of_nodes())
print("Number of connections (edges):", G.number_of_edges())

print("\nDegree of each station:")
for station, degree in G.degree():
    print(f"{station}: {degree}")
