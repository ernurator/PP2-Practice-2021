# https://leetcode.com/problems/number-of-good-pairs/submissions/
class Solution:
    def numIdenticalPairs(self, nums) -> int:
        cnt = 0
        for j in range(len(nums)):
            for i in range(j):
                if nums[i] == nums[j]:
                    cnt += 1
        return cnt