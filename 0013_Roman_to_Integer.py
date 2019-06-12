class Solution:
    def romanToInt(self, s: str) -> int:
        rule = {'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000}
        
        num = list(s)
        l = len(num)
        #Initialize the final result to zero
        result = 0
        
        #Compare each character in Roman from left to right
        #If it is greater than or equal to the left, it should be added
        #Otherwise it should be subtracted
        for i in range(l-1):
            if rule[num[i]]>=rule[num[i+1]]:
                result += rule[num[i]]
            else:
                result -= rule[num[i]]
        
        result += rule[num[l-1]]
        return result
