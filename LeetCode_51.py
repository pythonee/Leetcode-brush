class Solution(object):
    def solveNQueens(self, n):
        def _solve(n, row, curr, ans):
            if row == n:
                ans.append(list(curr))
                return

            for col in range(0, n):
                if col in self.col or row + col in self.pie or row - col in self.na:
                    continue

                self.col.add(col)
                self.pie.add(row + col)
                self.na.add(row - col)

                curr.append(col)

                _solve(n, row + 1, curr, ans)

                curr.pop()

                self.col.remove(col)
                self.pie.remove(row + col)
                self.na.remove(row - col)

        def _generate_result(ans, n):
            return [["." * (col) + "Q" + "." * (n - col - 1) for col in board] for board in ans]

        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.col = set()
        self.pie = set()
        self.na = set()

        ans = []

        _solve(n, 0, [], ans)

        board = _generate_result(ans, n)

        return board