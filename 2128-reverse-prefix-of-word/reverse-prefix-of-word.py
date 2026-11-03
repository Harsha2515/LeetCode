class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        words = ''
        count = 1
        for i in word:
            words += i
            if i == ch and count == 1:
                words = words[::-1]
                count -= 1
        return words
