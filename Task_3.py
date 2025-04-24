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

graph = {}

for u, v, weight in connections_with_weights:
    graph.setdefault(u, {})[v] = weight
    graph.setdefault(v, {})[u] = weight

def dijkstra(graph, current):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[current] = 0
    unvisited = list(graph.keys())

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances

print("Shortest paths (with weights) between all vertices:")

for node in graph:
    shortest = dijkstra(graph, node)
    for target, length in shortest.items():
        print(f"From {node} to {target}: {length}")