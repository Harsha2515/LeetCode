# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []

        def postorder(node):
            if node is None:
                return
            
            result.append(node.val)
            postorder(node.right)
            postorder(node.left)
        postorder(root)
        return result[::-1]