class Solution(object):
    def __init__(self):
        self.ans = []

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self._permute(nums, 0, len(nums), [])
        return self.ans


    def _permute(self, nums, level, MAX, group):
        if level >= MAX:
            self.ans.append(list(group))
            return

        for i in range(0, MAX):
            if nums[i] in group:
                continue

            group.append(nums[i])
            self._permute(nums, level + 1, MAX, group)
            group.pop()