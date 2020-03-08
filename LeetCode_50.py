class Solution:
    def myPow(self, x: float, n: int) -> float:
        r = 0

        if n < 0:
            return 1 / self.helper(x, 0-n)

        return self.helper(x, n)





    def helper(self, x, n):
        if n == 0: return 1
        if n == 1: return x

        if n % 2 == 0:
            sub_problem = n / 2
        else:
            sub_problem = (n-1) / 2


        sub_result = self.myPow(x, sub_problem)

        if n % 2 != 0:
            return  sub_result * sub_result * x

        return sub_result * sub_result