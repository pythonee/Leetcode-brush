class Solution(object):

    def __init__(self):
        self.cache = {}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.helper(n, 0)

    def helper(self, n, i):
        if i == n:
            return 1

        if i > n:
            return 0

        if i in self.cache:
            return self.cache[i]

        a = self.helper(n, i+1)
        b = self.helper(n, i+2)

        self.cache[i] = a + b
        return  a+b