class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        result = ''
        for i in words:
            result += i[::-1] + ' '
        return result.rstrip()