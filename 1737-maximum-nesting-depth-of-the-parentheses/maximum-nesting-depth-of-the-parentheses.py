class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        n = len(s)
        stack = []
        max_len = 0
        while i<n:
            if s[i] == '(':
                stack.append(s[i])
            elif s[i] == ')':
                stack.pop()
            max_len = max(max_len,len(stack))
            i+=1
        return max_len
