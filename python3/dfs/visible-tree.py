from typing import List, Union, Tuple, Any

from node import Node
from buid_node import build_tree


def visible_tree_node(root: Node) -> int:
    if not root:
        return 0
    def dfs(node, target):
        if node is None:
            return 0
        lr = dfs(node.left, max(target, node.val))
        rr = dfs(node.right, max(target, node.val))
        return lr + rr + (1 if node.val >= target else 0)

    return dfs(root, root.val)


if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = visible_tree_node(root)
    print(res)
