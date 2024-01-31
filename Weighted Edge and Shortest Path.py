import heapq

class Edge:
    def __init__(self, node1, node2, distance):
        # Initialize an edge with two nodes and a distance
        self.node1 = node1
        self.node2 = node2
        self.distance = distance

class Graph:
    def __init__(self):
        # Initialize an empty dictionary to store the adjacency list
        self.adjacency_list = {}
        # Initialize an empty list to store edges
        self.edges = []

    def add_node(self, node):
        # Add a node to the graph if it doesn't already exist
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2, distance):
        # Add an undirected edge between node1 and node2 with a given distance
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)
        # Create and append an edge to the list of edges
        self.edges.append(Edge(node1, node2, distance))

    def shortest_path(self, start, target):
        # Dijkstra's algorithm to find the shortest path
        distances = {node: float('inf') for node in self.adjacency_list}
        distances[start] = 0
        priority_queue = [(0, start)]
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_node == target:
                break

            if current_distance > distances[current_node]:
                continue

            for neighbor in self.adjacency_list[current_node]:
                distance_to_neighbor = distances[current_node] + self.get_distance(current_node, neighbor)
                if distance_to_neighbor < distances[neighbor]:
                    distances[neighbor] = distance_to_neighbor
                    heapq.heappush(priority_queue, (distance_to_neighbor, neighbor))

        path = self.reconstruct_path(start, target, distances)
        return path

    def reconstruct_path(self, start, target, distances):
        # Reconstruct the shortest path from start to target
        path = []
        current = target
        while current != start:
            path.insert(0, current)
            current = min(self.adjacency_list[current], key=lambda neighbor: distances[neighbor])
        path.insert(0, start)
        return path

    def all_paths(self, start, target):
        # Find all paths between start and target
        all_paths = []
        self.find_paths(start, target, [start], all_paths)
        return all_paths

    def find_paths(self, current, target, path, all_paths):
        # Recursively find all paths
        if current == target:
            all_paths.append(path.copy())
            return

        for neighbor in self.adjacency_list[current]:
            if neighbor not in path:
                self.find_paths(neighbor, target, path + [neighbor], all_paths)

    def get_distance(self, node1, node2):
        # Helper method to get the distance between two nodes
        for edge in self.edges:
            if (edge.node1 == node1 and edge.node2 == node2) or (edge.node1 == node2 and edge.node2 == node1):
                return edge.distance
        return None

# Example usage:
graph = Graph()
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_edge("A", "B", 3)
graph.add_edge("B", "C", 2)
graph.add_edge("A", "C", 5)

shortest_path = graph.shortest_path("A", "C")
print("Shortest Path:", shortest_path)

all_paths = graph.all_paths("A", "C")
print("All Paths:", all_paths)
