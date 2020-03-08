class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        key = {}
        key[2] = "abc"
        key[3] = "def"
        key[4] = "ghi"
        key[5] = "jkl"
        key[6] = "mno"
        key[7] = "pqrs"
        key[8] = "tuv"
        key[9] = "wxyz"

        ans = []
        self.search(digits, 0, key, "", ans)
        return ans

    def search(self, digits, level, key, group, ans):
        if len(digits) == 0:
            return

        if level == len(digits):
            ans.append(group)
            return

        letters = key[int(digits[level])]
        for letter in letters:
            self.search(digits, level + 1, key, group + letter, ans)
