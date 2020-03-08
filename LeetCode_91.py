class Solution(object):

    def __init__(self):
        self.cache = {}

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self._recur(s, 0, len(s))

    def _recur(self, s, start, MAX):
        if start == MAX:
            return 1

        if s[start] == "0":
            return 0

        if start in self.cache:
            return self.cache[start]

        a = self._recur(s, start + 1, MAX)
        b = 0

        if start < MAX - 1:
            tmp = s[start] + s[start + 1]
            if int(tmp) <= 26:
                b = self._recur(s, start + 2, MAX)

        self.cache[start] = a+b
        return a+b
