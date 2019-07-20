class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            fib = [1,2]
            i = 2
            while(i < n):
                fib.append(fib[i-2]+fib[i-1])
                i += 1
            return fib[-1]
