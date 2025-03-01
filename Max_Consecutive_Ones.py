class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a = len(nums)
        count = 0
        maxx = 0
        for i in range(0,a):
            if nums[i] == 1:
                count += 1
                maxx = max(maxx, count)
            else:
                count = 0
        return maxx