import networkx as nx
from collections import deque


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

def recursive_dfs(graph, current, target, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(current)
    path.append(current)

    if current == target:
        return path

    for neighbor in sorted(graph.neighbors(current)):
        if neighbor not in visited:
            result = recursive_dfs(graph, neighbor, target, visited, path)
            if result:
                return result

    path.pop()
    return None

def recursive_bfs(graph, current, target, queue=None, visited=None):
    if visited is None:
        visited = set()
    if queue is None:
        queue = deque([(current, [current])])

    if not queue:
        return None

    current, path = queue.popleft()

    if current == target:
        return path

    visited.add(current)

    for neighbor in sorted(graph.neighbors(current)):
        if neighbor not in visited and neighbor not in [node for node, _ in queue]:
            queue.append((neighbor, path + [neighbor]))

    return recursive_bfs(graph, current, target, queue, visited)

dfs_node_path = recursive_dfs(G, start_station, end_station)
bfs_node_path = recursive_bfs(G, start_station, end_station)

# Print results
print("DFS Path from", start_station, "to", end_station, ":", dfs_node_path)
print("BFS Path from", start_station, "to", end_station, ":", bfs_node_path)