# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        encoded = []

        def visit(node):
            if node:
                encoded.append(str(node.val))
                visit(node.left)
                visit(node.right)

        visit(root)
        return ' '.join(encoded)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if len(data) == 0:
            return
        nums = [int(val) for val in data.split()]
        root = TreeNode(nums[0])
        for i in range(1, len(nums)):
            self.tree_insert(root, nums[i])
        return root

    def tree_insert(self, root: TreeNode, val: int):
        inserted = False
        node = TreeNode(val)
        while not inserted:
            if val >= root.val:
                if root.right:
                    root = root.right
                else:
                    root.right = node
                    inserted = True
            else:
                if root.left:
                    root = root.left
                else:
                    root.left = node
                    inserted = True


# create a tree for test purposes
my_root = TreeNode(5)
my_root.left = TreeNode(3)
my_root.right = TreeNode(10)
node = my_root.left
node.left = TreeNode(2)
node = my_root.right
node.left = TreeNode(8)
node.right = TreeNode(11)

# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
tree = ser.serialize(my_root)
print(tree)
ans = deser.deserialize(tree)
# return ans
