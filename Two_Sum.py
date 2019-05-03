class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        i = 0
        loop = True
        while i<(length-1) and loop == True:
            j = i+1
            while j<length:
                if (nums[i]+nums[j]) == target:
                    return [i, j]
                    loop = False
                    break
                else:
                    j += 1
            i += 1
            if i == length-1:
                return None
                break
