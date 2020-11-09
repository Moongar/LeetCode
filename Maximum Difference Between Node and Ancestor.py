# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def __init__(self):
    #     self.result = 0

    def maxAncestorDiff(self, root: TreeNode) -> int:
        return self.dfs(root, root.val, root.val, 0)

    def dfs(self, root, min_ans, max_ans, diff):
        if not root:
            return diff
        diif = max(abs(root.val-min_ans), abs(root.val-max_ans), diff)
        min_ans = min(min_ans, root.val)
        max_ans = max(max_ans, root.val)
        diff_left = self.dfs(root.left, min_ans, max_ans, diff)
        deff_right = self.dfs(root.right, min_ans, max_ans, diff)
        return max(diif, diff_left, deff_right)


# rt = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))),
#               TreeNode(10, TreeNode(14, TreeNode(13))))
rt = TreeNode(1, TreeNode(2, TreeNode(0, TreeNode(3))))
s = Solution()
print(s.maxAncestorDiff(rt))
