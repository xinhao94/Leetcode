class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = 1
        #Use this while loop to count how many consecutive nine(9)s are
        #there at the end of the list, and record in variable "(i-1)"
        while i <= len(digits):
            if digits[-i] == 9:
                i += 1
                continue
            else:
                break
        
        #If there is no nine(9) at the end, then simply plus one to the
        #last element in the list
        if (i-1) == 0:
            digits[-1] += 1
        #Else if the list is consist of all nine(9)s, insert a leading one(1)
        #as the first element, and convert all other elements to zero(0)
        elif (i-1) == len(digits):
            digits.insert(0, 1)
            j = 1
            while j < len(digits):
                digits[j] = 0
                j += 1
        #Else if there is only a limited number of nine(9)s at the end, convert
        #all those nine(9)s to zero(0), and plus one to the digit immediately
        #before the first nine(9) in the consecutive nine(9) sequence.
        else:
            j = 1
            while j <= (i-1):
                digits[-j] = 0
                j += 1
            digits[-i] += 1
            
        return digits
