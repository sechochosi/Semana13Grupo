from arbol import insert

def pre_order_traversal(node):
    if not node:
        return
    print(f"{node.key} (H={node.height}) ", end="")
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)

def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.key))
        if root.left:
            print_tree(root.left, level + 1, "L--- ")
        if root.right:
            print_tree(root.right, level + 1, "R--- ")

if __name__ == "__main__":
    root = None

    keys = [10, 20, 30, 40, 50, 25]

    for key in keys:
        print(f"Inserting {key}:")
        root = insert(root, key)
        print_tree(root)
        print("\n")
