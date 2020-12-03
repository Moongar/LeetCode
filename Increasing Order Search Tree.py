# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        vals = self.sort_tree(root, [])
        new_root = TreeNode(vals[0])
        node = new_root
        for val in vals[1:]:
            node.right = TreeNode(val)
            node = node.right
        return new_root

    def sort_tree(self, node, sorted_vals):
        if node:
            self.sort_tree(node.left, sorted_vals)
            sorted_vals.append(node.val)
            self.sort_tree(node.right, sorted_vals)
        return sorted_vals


s = Solution()
my_root = TreeNode(5, TreeNode(3), TreeNode(8))
print(s.increasingBST(my_root))
