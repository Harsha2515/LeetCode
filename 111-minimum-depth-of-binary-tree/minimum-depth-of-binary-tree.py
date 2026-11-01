class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        count = float('inf')

        def dfs(node, depth):
            nonlocal count

            if not node:
                return

            if not node.left and not node.right:
                count = min(count, depth)
                return

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        if not root:
            return 0

        dfs(root, 1)
        return count