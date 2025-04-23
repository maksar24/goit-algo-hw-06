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

start_station = "Bond Street"
end_station = "Leicester Square"

dfs_path = list(nx.dfs_edges(G, source=start_station))
bfs_path = list(nx.bfs_edges(G, source=start_station))
shortest = nx.shortest_path(G, source=start_station, target=end_station)

def edge_list_to_node_path(edge_list, target):
    path = [edge_list[0][0]]
    for station1, station2 in edge_list:
        path.append(station2)
        if station2 == target:
            break
    return path

dfs_node_path = edge_list_to_node_path(dfs_path, end_station)
bfs_node_path = edge_list_to_node_path(bfs_path, end_station)

# Print results
print("DFS Path from", start_station, "to", end_station, ":", dfs_node_path)
print("BFS Path from", start_station, "to", end_station, ":", bfs_node_path)
print("True Shortest Path:", shortest)