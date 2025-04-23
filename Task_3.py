import networkx as nx


connections_with_weights = [
    ("Bond Street", "Oxford Circus", 2),
    ("Bond Street", "Green Park", 4),
    ("Oxford Circus", "Green Park", 1),
    ("Green Park", "Piccadilly Circus", 3),
    ("Piccadilly Circus", "Oxford Circus", 1),
    ("Piccadilly Circus", "Leicester Square", 2),
    ("Oxford Circus", "Tottenham Court Road", 2),
    ("Leicester Square", "Tottenham Court Road", 1),
    ("Leicester Square", "Covent Garden", 2),
    ("Covent Garden", "Holborn", 1),
    ("Holborn", "Tottenham Court Road", 3),
]

G = nx.Graph()

for station1, station2, weight in connections_with_weights:
    G.add_edge(station1, station2, weight=weight)

shortest_paths = nx.all_pairs_dijkstra_path_length(G)

print("Shortest paths (with weights) between all vertices:")
for source, target_dict in shortest_paths:
    for target, length in target_dict.items():
        print(f"From {source} to {target}: {length}")