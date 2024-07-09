from math import inf

from buid_node import build_tree
from node import Node


def valid_bst(root: Node) -> bool:
    if not root:
        return True

    def dfs(tree, min_value, max_value):
        if tree is None:
            return True
        if not (min_value < tree.val < max_value):
            return False
        return dfs(tree.left, min_value, tree.val) and dfs(tree.right, tree.val, max_value)
    return dfs(root, -inf, inf)


if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = valid_bst(root)
    print('true' if res else 'false')
