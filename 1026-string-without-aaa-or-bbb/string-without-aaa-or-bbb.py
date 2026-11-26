class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        result = []

        while a > 0 or b > 0:

            if result[-2:] == ['a', 'a']:
                result.append('b')
                b -= 1

            elif result[-2:] == ['b', 'b']:
                result.append('a')
                a -= 1

            elif a >= b:
                result.append('a')
                a -= 1

            else:
                result.append('b')
                b -= 1

        return ''.join(result)