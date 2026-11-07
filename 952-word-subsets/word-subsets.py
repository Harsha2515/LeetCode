from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        required = Counter()

        # Find maximum frequency requirement for each character
        for word in words2:
            freq = Counter(word)

            for char, count in freq.items():
                required[char] = max(required[char], count)

        result = []

        # Check each word in words1
        for word in words1:
            freq = Counter(word)

            if all(freq[char] >= count for char, count in required.items()):
                result.append(word)

        return result