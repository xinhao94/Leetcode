class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            local_max = nums[0]
            global_max = nums[0]
            i = 1
            while i < len(nums):
                local_max = max(local_max+nums[i], nums[i])
                global_max = max(local_max, global_max)
                i += 1
            return global_max
