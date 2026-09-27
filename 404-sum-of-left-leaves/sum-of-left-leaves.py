class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:

        def leftNode(node):
            if node is None:
                return 0

            total = 0

            # Check if left child exists and is a leaf
            if node.left and node.left.left is None and node.left.right is None:
                total += node.left.val

            total += leftNode(node.left)
            total += leftNode(node.right)

            return total

        return leftNode(root)