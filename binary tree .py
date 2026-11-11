"""
Assessment 3.3: Non-linear Data Structures
Diagram 2: Binary Tree (level-order BFS and preorder DFS)

Structure:
Level 0:        P
Level 1:     A     N
Level 2:   S   A  C   A
Level 3: L   A
"""

from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree():
    """P -> (A, N); A -> (S, A); S -> (L, A); N -> (C, A)."""
    root = TreeNode("P")
    root.left, root.right = TreeNode("A"), TreeNode("N")
    root.left.left, root.left.right = TreeNode("S"), TreeNode("A")
    root.left.left.left = TreeNode("L")
    root.left.left.right = TreeNode("A")
    root.right.left, root.right.right = TreeNode("C"), TreeNode("A")
    return root


def tree_bfs(root):
    """Algorithm C: Level-Order Traversal (BFS)."""
    order = []

    # Step 1: Start. If the root is empty, stop.
    if root is None:
        return order

    # Step 2: Prepare. Create an empty queue.
    queue = deque()

    # Step 3: Enqueue the root.
    queue.append(root)

    # Step 4: Check the queue. Stop looping when it is empty.
    while queue:
        # Step 5: Dequeue the front node and add it to the output.
        node = queue.popleft()
        order.append(node.value)

        # Step 6: Enqueue the left child, then the right child.
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        # Step 7: Repeat. The while loop goes back to Step 4.

    # Step 8: Display and end.
    return order


def tree_dfs(node, order=None):
    """Algorithm D: Preorder Traversal (DFS)."""
    # Step 1: Start. Begin at the root (first call).
    if order is None:
        order = []

    # Step 2: Check the node. If it is empty, return.
    if node is None:
        return order

    # Step 3: Visit the node and add its value to the output.
    order.append(node.value)

    # Step 4: Go left.
    tree_dfs(node.left, order)

    # Step 5: Go right.
    tree_dfs(node.right, order)

    # Step 6: Display and end (the caller prints the result).
    return order


if __name__ == "__main__":
    root = build_tree()
    print("=== Diagram 2: Binary Tree ===")
    print("BFS (level-order):", " -> ".join(tree_bfs(root)))
    print("DFS (preorder):   ", " -> ".join(tree_dfs(root)))