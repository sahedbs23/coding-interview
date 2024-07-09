from node import Node
from buid_node import build_tree


def is_balanced_binary_tree(root: Node) -> bool:
    def dfs(linked_list: Node):
        if not linked_list:
            return 0
        left_diff = dfs(linked_list.left)
        right_diff = dfs(linked_list.right)
        if left_diff == -1 or right_diff == -1:
            return -1
        if abs(left_diff-right_diff) > 1:
            return -1
        return max(left_diff, right_diff) + 1
    return dfs(root) != -1


if __name__ == '__main__':
    tree = build_tree(iter(input().split()), int)
    res = is_balanced_binary_tree(tree)
    print('true' if res else 'false')

