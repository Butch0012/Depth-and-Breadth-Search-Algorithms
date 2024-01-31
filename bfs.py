from collections import deque

class Graph:
    def __init__(self):
        # Initialize an empty adjacency list for the graph
        self.adjacency_list = {}

    def add_node(self, node):
        # Add a new node to the graph's adjacency list
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2):
        # Add an undirected edge between two nodes in the graph
        if node1 in self.adjacency_list and node2 in self.adjacency_list:
            self.adjacency_list[node1].append(node2)
            self.adjacency_list[node2].append(node1)

    def breadth_first_reachable(self, starting_node, target_node):
        # Check if nodes exist in the graph
        if starting_node not in self.adjacency_list or target_node not in self.adjacency_list:
            return False

        # Initialize queue with the starting node
        queue = deque([starting_node])
        # Keep track of traversed nodes to avoid infinite loops
        traversed_nodes = set()

        # Loop until the queue is empty
        while queue:
            # Take the first element from the queue
            current_node = queue.popleft()

            # Check if the current node is the target node
            if current_node == target_node:
                return True  # Target node is reachable
            else:
                # Flag the current node as traversed
                traversed_nodes.add(current_node)

                # Get the adjacency list for the current node
                adjacency_list = self.adjacency_list[current_node]

                # Explore each adjacent node
                for node in adjacency_list:
                    if node not in traversed_nodes:
                        queue.append(node)  # Add untraversed nodes to the queue

        # If the queue is empty and the target node hasn't been found, it's not reachable
        return False

# Example usage:
graph = Graph()
graph.add_node("Jasmine")
graph.add_node("Ada")
graph.add_node("Lydia")
graph.add_node("Rose")
graph.add_node("Dylan")
graph.add_node("Allison")
graph.add_node("Thomas")
graph.add_edge("Jasmine", "Ada")
graph.add_edge("Jasmine", "Lydia")
graph.add_edge("Jasmine", "Rose")
graph.add_edge("Ada", "Dylan")
graph.add_edge("Lydia", "Ada")
graph.add_edge("Dylan", "Allison")
graph.add_edge("Lydia", "Thomas")

# Test cases
print(graph.breadth_first_reachable("Jasmine", "Ada"))  # True
print(graph.breadth_first_reachable("Jasmine", "Sarah"))  # False
