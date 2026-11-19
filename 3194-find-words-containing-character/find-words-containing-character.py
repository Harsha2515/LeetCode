class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        out = []
        for i in range(len(words)):
            for ch in words[i]:
                if ch == x:
                    out.append(i)
                    break
        return out