class Solution(object):
    def sumFourDivisors(self, nums):
        total = 0

        for n in nums:
            divisors = []

            i = 1
            while i * i <= n:
                if n % i == 0:
                    divisors.append(i)

                    if i != n // i:
                        divisors.append(n // i)

                    # More than 4 means we don't need this number
                    if len(divisors) > 4:
                        break

                i += 1

            if len(divisors) == 4:
                total += sum(divisors)

        return total