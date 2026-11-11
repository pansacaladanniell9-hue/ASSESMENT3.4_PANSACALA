"""
Assessment 3.3: Non-linear Data Structures
Diagram 1: PANSACALA Graph (BFS and DFS)
"""

from collections import deque

# The four A's are separate nodes: A2, A5, A7, A9 (position in the name)
NAME_ORDER = ["P", "A", "N", "S", "A", "C", "A", "L", "A"]

EDGES = [
    ("P", "A"), ("P", "N"), ("A", "N"), ("N", "S"), ("N", "C"),
    ("S", "A"), ("A", "C"), ("C", "A"), ("C", "L"),
    ("A", "L"), ("L", "A"),
]


def build_graph():
    """Build an adjacency list; neighbors sorted in PANSACALA order."""
    graph = {node: [] for node in NAME_ORDER}
    for u, v in EDGES:
        graph[u].append(v)
        graph[v].append(u)
    for node in graph:
        graph[node].sort(key=NAME_ORDER.index)
    return graph


def graph_bfs(graph, start):
    """Algorithm A: Breadth-First Search."""
    # Step 1: Start. Begin at the start node.
    # Step 2: Prepare. Create an empty queue and an empty visited list.
    queue = deque()
    visited = []
    order = []

    # Step 3: Enqueue the start node and mark it visited.
    queue.append(start)
    visited.append(start)

    # Step 4: Check the queue. Stop looping when it is empty.
    while queue:
        # Step 5: Dequeue the front node and add it to the output order.
        node = queue.popleft()
        order.append(node)

        # Step 6: Visit neighbors. Enqueue each unvisited neighbor.
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
        # Step 7: Repeat. The while loop goes back to Step 4.

    # Step 8: Display and end.
    return order


def graph_dfs(graph, start):
    """Algorithm B: Depth-First Search."""
    # Step 1: Start. Begin at the start node.
    # Step 2: Prepare. Create an empty stack and an empty visited list.
    stack = []
    visited = []
    order = []

    # Step 3: Push the start node onto the stack.
    stack.append(start)

    # Step 4: Check the stack. Stop looping when it is empty.
    while stack:
        # Step 5: Pop the top node. Skip it if already visited.
        node = stack.pop()
        if node in visited:
            continue

        # Step 6: Visit. Mark the node visited and add it to the output.
        visited.append(node)
        order.append(node)

        # Step 7: Push unvisited neighbors in reverse order so the
        #         earliest letter in PANSACALA is popped first.
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)
        # Step 8: Repeat. The while loop goes back to Step 4.

    # Step 9: Display and end.
    return order


if __name__ == "__main__":
    graph = build_graph()
    print("=== Diagram 1: PANSACALA Graph ===")
    print("Adjacency list:")
    for node, neighbors in graph.items():
        print(f"  {node}: {neighbors}")
    print("BFS:", " -> ".join(graph_bfs(graph, "P")))
    print("DFS:", " -> ".join(graph_dfs(graph, "P")))