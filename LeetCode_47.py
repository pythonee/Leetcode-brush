class Solution(object):

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        used = [False]* len(nums)
        ans = []
        sorted_nums = sorted(nums)
        self._permuteUnique(sorted_nums, 0, len(nums), used, [], ans)
        return ans

    def _permuteUnique(self, nums, level, MAX, used, group, ans):
        if level >= MAX:
            ans.append(list(group))
            return ans

        for i in range(0, MAX):
            if used[i]: continue
            if (i >0 and nums[i] == nums[i-1] and used[i-1]) : continue

            group.append(nums[i])
            used[i] = True
            self._permuteUnique(nums, level+1, MAX, used, group, ans)
            group.pop()
            used[i] = False