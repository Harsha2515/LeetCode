class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        sum1 = 0
        for i in firstWord:
            sum1 *= 10
            sum1 += ord(i) - 97
        sum2 = 0
        for i in secondWord:
            sum2 *= 10
            sum2 += ord(i) - 97
        
        target = 0
        for i in targetWord:
            target *= 10
            target += ord(i) - 97
        
        return sum1 + sum2 == target