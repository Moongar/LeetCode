# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root.left and not root.right:
            return root
        deepest_nodes = []
        parent = {}
        levels = {}
        level = 0
        max_level = self.dfs(root, 0, levels, parent)
        deep_nodes = [node for node in levels.keys() if levels[node] == max_level]
        if len(deep_nodes) == 1:
            return deep_nodes[0]
        parents = set([parent[node] for node in deep_nodes])
        while len(parents) > 1:
            parents = set([parent[node] for node in parents])

        return list(parents)[0]

    def dfs(self, node, level, levels, parent):
        if node.left:
            parent[node.left] = node
            levels[node.left] = level + 1
            max_level_left = max(level + 1, self.dfs(node.left, level + 1, levels, parent))
        else:
            max_level_left = level
        if node.right:
            parent[node.right] = node
            levels[node.right] = level + 1
            max_level_right = max(level + 1, self.dfs(node.right, level + 1, levels, parent))
        else:
            max_level_right = level

        return max(max_level_left, max_level_right)
