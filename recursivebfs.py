from collections import deque

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

    def recursive_bfs(self, queue, target, visited=None):
        # Implement recursive Breadth-First Search (BFS) to find a path from the front of the queue to the target

        # If visited is not provided, initialize it as an empty set
        if visited is None:
            visited = set()

        # Check if the queue is empty
        if not queue:
            return None

        # Pop the leftmost element from the queue
        current = queue.popleft()

        # Mark the current node as visited
        visited.add(current)

        # If the current node is the target, return a path containing only the current node
        if current == target:
            return [current]

        # Explore neighbors of the current node
        for neighbor in self.adjacency_list[current]:
            # Check if the neighbor has not been visited
            if neighbor not in visited:
                # Append the neighbor to the queue for further exploration
                queue.append(neighbor)

                # Recursively search for a path from the neighbor to the target
                path = self.recursive_bfs(queue, target, visited)

                # If a path is found, prepend the current node and return the path
                if path:
                    return [current] + path

        # If no path is found, return None
        return None
