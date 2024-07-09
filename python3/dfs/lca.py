from node import Node
from buid_node import build_tree


def lca_on_bst(bst: Node, p: int, q: int) -> int:
    if p <= bst.val and q <= bst.val:
        return lca_on_bst(bst.left, p, q)
    elif p > bst.val and q > bst.val:
        return lca_on_bst(bst.right, p, q)
    else:
        return bst.val


if __name__ == '__main__':
    bst = build_tree(iter(input().split()), int)
    p = int(input())
    q = int(input())
    res = lca_on_bst(bst, p, q)
    print(res)
