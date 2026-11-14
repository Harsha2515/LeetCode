class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        arr1 = [0] * 26
        arr2 = [0] * 26
        arr3 = [0] * 26

        for ch in word1:
            arr1[ord(ch)-97] += 1
        for ch in word2:
            arr2[ord(ch)-97] += 1
        
        for i in range(26):
            arr3.append(abs(arr1[i]-arr2[i]))
        
        return max(arr3)<=3