class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(s, open_count, close_count):
            # A complete valid combination
            if open_count == n and close_count == n:
                result.append(s)
                return

            # Add '('
            if open_count < n:
                backtrack(s + "(", open_count + 1, close_count)

            # Add ')'
            if close_count < open_count:
                backtrack(s + ")", open_count, close_count + 1)

        backtrack("", 0, 0)

        return result