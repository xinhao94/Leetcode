class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #If input is an empty list, return zero
        if len(nums) == 0:
            return 0
        #Else if input list has only one element,
        #return this single element
        elif len(nums) == 1:
            return nums[0]
        #Else, use dynamic programming (DP) method ->
        #Specifically, Kadane algorithm
        else:
            #Variable "local_max" represents the max sum of a subset of lists.
            #In this subset, all lists end with "nums[i-1]" (in "i"th iteration).
            local_max = nums[0]
            #Variable "global_max" record the max value of all "local_max" variables
            #through all iterations.
            global_max = nums[0]
            i = 1
            while i < len(nums):
                #The "local_max" variable of each iteration is calculated based on the
                #variable "local_max" from previous iteration. If the previous "local_max"
                #is positive, then the new "local_max" is "nums[i]" plus the previous
                #"local_max". If the previous "local_max" is negative, then the new
                #"local_max" is simply "nums[i]" itself.
                local_max = max(local_max+nums[i], nums[i])
                #If the new "local_max" generated from this iteration is larger than the
                #largest value of all "local_max" variables ever recorded, then the variable
                #"global_max" will be updated by this new largest value.
                global_max = max(local_max, global_max)
                i += 1
            return global_max
