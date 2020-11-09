# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        tilt = {}
        w = {}
        self.dfs(root, tilt, w)
        return sum(tilt.values())

    def dfs(self, node, tilt, w):
        if not node.left and not node.right:
            tilt[node] = 0
            w[node] = node.val
        elif not node.left:
            self.dfs(node.right, tilt, w)
            w[node] = w[node.right] + node.val
            tilt[node] = abs(w[node.right])
        elif not node.right:
            self.dfs(node.left, tilt, w)
            w[node] = w[node.left] + node.val
            tilt[node] = abs(w[node.left])
        else:
            self.dfs(node.right, tilt, w)
            self.dfs(node.left, tilt, w)
            w[node] = w[node.left] + w[node.right] + node.val
            tilt[node] = abs(w[node.left] - w[node.right])


# rt = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(5)), TreeNode(9, TreeNode(7)))
s = Solution()
print(s.findTilt(TreeNode(None)))
