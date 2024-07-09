from typing import List


class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children


def ternary_tree_paths(root: Node) -> List[str]:
    def dfs(node: Node, path, response):
        if all(r is None for r in node.children):
            response.append('->'.join(path) + '->' + str(node.val))
        for child in node.children:
            if child is not None:
                dfs(child, path + [str(node.val)], response)
    response = []
    dfs(root, [], response)
    return response


# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)


if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = ternary_tree_paths(root)
    for line in res:
        print(line)
