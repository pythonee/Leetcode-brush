class Solution:
    def __init__(self):
        self.ans = None

    def combine(self, n, k):

        if k > n:
            return None

        self.ans = []
        self._combine(1, n, k, [])
        return self.ans


    def _combine(self, start, end, k, group):
        if not k:
            self.ans.append(list(group))
            return

        if (end - start + 1) < k:
            return

        for i in range(start, end + 1):
            group.append(i)
            self._combine(i + 1, end, k-1, group)
            group.pop()
