class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        k = len(s)
        if k % 2 != 0:
            return False
        for i in range(k):
            if s[i] == '[' or s[i] =='(' or s[i] == '{':
                stack.append(s[i])
            if s[i] == '}':
                if len(stack) == 0:
                    return False
                t = stack.pop()
                if t!='{':
                    return False
            if s[i] == ')':
                if len(stack) == 0:
                    return False
                t = stack.pop()
                if t!='(':
                    return False
            if s[i] == ']':
                if len(stack) == 0:
                    return False
                t = stack.pop()
                if t!='[':
                    return False
        if len(stack) != 0:
            return False
        return True
            