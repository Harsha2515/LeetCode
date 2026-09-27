class Solution:
    def findNthDigit(self, n: int) -> int:
        digits = 1
        count = 9
        start = 1

        # Find which digit-length group contains n
        while n > digits * count:
            n -= digits * count
            digits += 1
            count *= 10
            start *= 10

        # Find the actual number
        num = start + (n - 1) // digits

        # Find the digit inside that number
        index = (n - 1) % digits

        return int(str(num)[index])