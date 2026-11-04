from collections import deque

class Solution:
    def isCousins(self, root, x, y):

        queue = deque([root])

        while queue:
            size = len(queue)
            found_x = found_y = False

            for _ in range(size):
                node = queue.popleft()

                if node.val == x:
                    found_x = True

                if node.val == y:
                    found_y = True

                # Siblings cannot be cousins
                if node.left and node.right:
                    if (node.left.val == x and node.right.val == y) or \
                       (node.left.val == y and node.right.val == x):
                        return False

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            # Both found at the same level
            if found_x and found_y:
                return True

            # Only one found: different depths
            if found_x or found_y:
                return False

        return False