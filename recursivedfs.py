class Graph:
    def __init__(self):
        # Initialize an empty dictionary to store the adjacency list
        self.adjacency_list = {}

    def add_node(self, node):
        # Add a node to the graph if it doesn't already exist
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2):
        # Add an undirected edge between node1 and node2
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)

    def recursive_dfs(self, start, target, visited=None):
        # Implement recursive Depth-First Search (DFS) to find a path from start to target

        # If visited is not provided, initialize it as an empty set
        if visited is None:
            visited = set()

        # Mark the current node as visited
        visited.add(start)

        # If the start node is the target, return a path containing only the start node
        if start == target:
            return [start]

        # Explore neighbors of the current node
        for neighbor in self.adjacency_list[start]:
            # Check if the neighbor has not been visited
            if neighbor not in visited:
                # Recursively search for a path from the neighbor to the target
                path = self.recursive_dfs(neighbor, target, visited.copy())

                # If a path is found, prepend the current node and return the path
                if path:
                    return [start] + path

        # If no path is found, return None
        return None
