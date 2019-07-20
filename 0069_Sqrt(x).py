class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0;
        ans = 0
        while(ans**2 < x):
            ans += 1
        if ans**2 == x:
            return ans
        else:
            return ans-1
