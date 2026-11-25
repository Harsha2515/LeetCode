class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        result = []
        for s in sentences:
            result.append(len(s.split()))
        return max(result)