class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        while i < (len(nums) - 1):
            if nums[i] == nums[i+1]:
                del nums[i+1]
            else:
                i += 1
        return len(nums)
