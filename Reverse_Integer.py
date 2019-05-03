class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        if x>0:
            y = str(x)
            length = len(y)
            z = ''
            for i in range(length):
                z = z+y[length-1-i]
            result = int(z)
        else:
            x = -x
            y = str(x)
            length = len(y)
            z = ''
            for i in range(length):
                z = z+y[length-1-i]
            result = -int(z)
        if result>(2**31-1) or result<(-2**31):
            return 0
        else:
            return result
