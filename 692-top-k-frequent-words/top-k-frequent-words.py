class Solution:
    from collections import Counter

    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq = Counter(words)
        arr = []

        for _ in range(k):
            word = min(freq, key=lambda x: (-freq[x], x))
            arr.append(word)
            del freq[word]

        return arr