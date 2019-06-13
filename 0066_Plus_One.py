class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = 1
        while i <= len(digits):
            if digits[-i] == 9:
                i += 1
                continue
            else:
                break
        
        if (i-1) == 0:
            digits[-1] += 1
        elif (i-1) == len(digits):
            digits.insert(0, 1)
            j = 1
            while j < len(digits):
                digits[j] = 0
                j += 1
        else:
            j = 1
            while j <= (i-1):
                digits[-j] = 0
                j += 1
            digits[-i] += 1
            
        return digits
