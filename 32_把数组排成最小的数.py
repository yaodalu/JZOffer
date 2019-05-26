# -*- coding:utf-8 -*-

class Solution:
    def PrintMinNumber(self, numbers):
        newNumbers = sorted(numbers,cmp=self.cmp)
        return ''.join([str(i) for i in newNumbers])

    def cmp(self,number1,number2):
        if int(str(number1)+str(number2)) < int(str(number2)+str(number1)):             #如果3213 < 3321,就认为321<3,组合时321应当在3前面
            return -1
        else:
            return 1
    
if __name__ == "__main__":
    print Solution().PrintMinNumber([3,321,32])
