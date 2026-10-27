class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#'] * n for _ in range(m)]
        i, j = 0, 0
        grid[0][0] = '.'
        prefer_right = True  # alternate between moving right and moving down

        while i != m - 1 or j != n - 1:
            if prefer_right:
                if j + 1 < n:
                    j += 1
                else:
                    i += 1
            else:
                if i + 1 < m:
                    i += 1
                else:
                    j += 1
            grid[i][j] = '.'
            prefer_right = not prefer_right

        return [''.join(row) for row in grid]