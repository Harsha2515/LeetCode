class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n % 2 == 0:
            return list(range(-n/2,0)) + list(range(1,n/2 + 1))
        else:
            return list(range((-n+1)/2,(n+1)/2))