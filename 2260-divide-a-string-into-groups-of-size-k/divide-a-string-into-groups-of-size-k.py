class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        t = len(s) % k
        if t>0:
            s = s + fill * (k-t)
        result = []
        n = 0
        for i in range(len(s)//k):
            result.append(s[n:n+k])
            n += k
        return result