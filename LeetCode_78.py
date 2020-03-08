class Solution:
    def subsets(self, nums):
        ans = []
        self.dfs(nums, 0, [], ans)
        return ans

    def dfs(self, nums, index, group, ans):
        if index == len(nums):
            ans.append(list(group))
            return

        self.dfs(nums, index+1, group, ans)

        group.append(nums[index])
        self.dfs(nums, index+1, group, ans)

        group.pop()