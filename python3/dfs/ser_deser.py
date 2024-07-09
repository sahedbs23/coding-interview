from node import Node
from buid_node import build_tree


def serialize(root: Node) -> str:
    def dfs_serialize(btree):
        if not btree:
            return 'x'
        str1 = dfs_serialize(btree.left)
        str2 = dfs_serialize(btree.right)
        return str(btree.val) + ' ' + str1 + ' ' + str2

    return dfs_serialize(root)


def deserialize(s: str):
    def dfs(nodes):
        val = next(nodes)
        if not val or val == 'x':
            return
        currentNode = Node(int(val))
        currentNode.left = dfs(nodes)
        currentNode.right = dfs(nodes)
        return currentNode

    return dfs(iter(s.split()))


if __name__ == '__main__':
    def build_tree(nodes):
        val = next(nodes)
        if not val or val == 'x': return
        cur = Node(val)
        cur.left = build_tree(nodes)
        cur.right = build_tree(nodes)
        return cur


    def print_tree(root):
        if not root:
            yield "x"
            return
        yield str(root.val)
        yield from print_tree(root.left)
        yield from print_tree(root.right)


    root = build_tree(iter(input().split()))
    new_root = deserialize(serialize(root))
    print(' '.join(print_tree(new_root)))
