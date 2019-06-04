# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        if not s:
            return 0
        num,count = 0,1
        for i in range(len(s)-1,0,-1):            #利用123 = 1*100+2*10+3*1,从低位累加               
            if s[i] not in '1234567890':
                return 0
            else:
                num += int(s[i])*count
                count *= 10
        if s[0] in '1234567890':
            return int(s[0])*count+num
        if s[0] == '+':
            return num
        if s[0] == '-':
            return -1*num
        return 0

if __name__ == "__main__":
    print Solution().StrToInt('12345')
