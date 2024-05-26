from node import Node
from buid_node import build_tree


def inorder(tree: Node):
    if tree is not None:
        inorder(tree.left)
        print(tree.val)
        inorder(tree.right)


if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    inorder(root)
