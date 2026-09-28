class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        def sum_arr(arr):
            sum_a = 0
            for i in arr:
                sum_a += i
            return sum_a
        def dig(n):
            arr = []
            while n>0:
                arr.append(n%10)
                n//=10
            return arr
        count = 0
        for i in range(1,num+1):
            if sum_arr(dig(i)) % 2 == 0:
                count += 1
        return count