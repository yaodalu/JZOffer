class Solution:
    def jumpFloorII(self,number):   
        if number == 1:
            return 1
        a,res = 1,0
        for i in range(2,number+1):             
            res = 2*a                           #f(n)=2*f(n-1)
            a = res
        return res

if __name__ == "__main__":
    solution = Solution()
    print solution.jumpFloorII(4)
