class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            digit = 1
            while (x-10**digit)>=0:
                digit += 1
            result = True
            i = 1
            while i<(digit+1-i):
                num_down = int(x/(10**(i-1))%10)
                num_up = int(x/(10**(digit-i))%10)
                if num_down != num_up:
                    result = False
                    break
                i += 1
            return result  
