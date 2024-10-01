class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2, weight=1):
        if node1 in self.adjacency_list and node2 in self.adjacency_list:
            self.adjacency_list[node1].append((node2, weight))
            self.adjacency_list[node2].append((node1, weight))

    def bfs(self, start):
        visited = set()
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                print(node, end=" ")
                for neighbor, _ in self.adjacency_list[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

    def dfs(self, start):
        visited = set()
        self.dfs_helper(start, visited)

    def dfs_helper(self, node, visited):
        visited.add(node)
        print(node, end=" ")
        for neighbor, _ in self.adjacency_list[node]:
            if neighbor not in visited:
                self.dfs_helper(neighbor, visited)

    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.adjacency_list}
        distances[start] = 0
        priority_queue = [(0, start)]
        while priority_queue:
            distance, node = min(priority_queue)
            priority_queue.remove((distance, node))
            for neighbor, weight in self.adjacency_list[node]:
                new_distance = distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    priority_queue.append((new_distance, neighbor))
        return distances

    def bellman_ford(self, start):
        distances = {node: float('inf') for node in self.adjacency_list}
        distances[start] = 0
        for _ in range(len(self.adjacency_list) - 1):
            for node, neighbors in self.adjacency_list.items():
                for neighbor, weight in neighbors:
                    distances[neighbor] = min(distances[neighbor], distances[node] + weight)
        return distances


# Example usage:
graph = Graph()
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')

graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)
graph.add_edge('D', 'E', 3)

print("BFS traversal:")
graph.bfs('A')
print("\nDFS traversal:")
graph.dfs('A')
print("\nDijkstra's algorithm:")
print(graph.dijkstra('A'))
print("\nBellman-Ford algorithm:")
print(graph.bellman_ford('A'))
