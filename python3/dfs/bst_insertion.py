from node import Node
from buid_node import build_tree


def print_bst(root: Node):
    if not root:
        print('x')
        return
    print(root.val)
    print_bst(root.left)
    print_bst(root.right)


# 8 5 2 x 3 x x 6 x x 10 x 14 x x
def insert(root: Node, value: int):
    if not root:
        return Node(value)

    if root.val > value:
        root.left = insert(root.left, value)
    elif root.val < value:
        root.right = insert(root.right, value)
    return root


if __name__ == '__main__':
    tree = build_tree(iter(input().split()), int)
    res = insert(tree, 7)
    print_bst(res)
    # print(res.val if res is not None else 0)
