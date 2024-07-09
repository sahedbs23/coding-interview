from node import Node
from buid_node import build_tree


# 5 4 3 x x 6 x x 8 x x
def visit_node(root: Node):
    if not root:
        return
    stack = [root]
    while len(stack) > 0:
        item = stack.pop()
        print(item.val)
        if item.right is not None:
            stack.append(item.right)
        if item.left is not None:
            stack.append(item.left)


if __name__ == '__main__':
    tree = build_tree(iter(input().split()), int)
    visit_node(tree)
