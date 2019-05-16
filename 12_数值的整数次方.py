# -*- coding: utf-8 -*-
class Solution:
    def Power(self,base,exponent):
        if (base == 0) and exponent < 0:            #Python中的==判断值
            return 0
        return base**(exponent)

if __name__ == "__main__":
    solution = Solution()
    print solution.Power(0.0,-1)
