from node import Node


def dfs(root: Node, target):
    if root is None:
        return None

    if root.val == target:
        return root

    left = dfs(root.left, target)

    if left is not None:
        return left

    return dfs(root.right, target)
