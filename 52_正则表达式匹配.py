# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if s == '':                                                                                                                                         #空字符串
            if pattern == '' or (len(pattern)==2 and pattern.index('*')==1):
                return True
            return False
        if pattern == '':                                                                                                                                   #空模式串
            return False
        sP,patternP = 0,0
        return self.matchRecur(s,sP,pattern,patternP)
        
    def matchRecur(self,s,sP,pattern,patternP):
        if sP == len(s) and patternP == len(pattern):                                                                                                       #如果模式串和字符串全都匹配完毕
            return True
        if sP != len(s) and patternP == len(pattern):                                                                                                       #如果模式串到头,字符串未结束则匹配失败,如('aa','.')
            return False
        if patternP < len(pattern)-1 and pattern[patternP+1] == '*':                                                                                        #如果模式串的第二个字符是'*'
            if (sP < len(s) and s[sP] == pattern[patternP]) or ( sP < len(s) and pattern[patternP] == '.'):                                                 #如果通配符前的字符和字符串匹配,可能匹配次数为n,1,0
                """caution! Python数组防止溢出判断语句sP < len(s)要放在s[sP]前面"""
                return self.matchRecur(s,sP+1,pattern,patternP) or self.matchRecur(s,sP+1,pattern,patternP+2) or self.matchRecur(s,sP,pattern,patternP+2)
            else:                                                                                                                                           #如果通配符前的字符和字符串不匹配,匹配次数为0，patternP后移2位
                print 'test'
                return self.matchRecur(s,sP,pattern,patternP+2)
        else:
            if (sP < len(s) and s[sP] == pattern[patternP]) or ( sP < len(s) and pattern[patternP] == '.'):
                return self.matchRecur(s,sP+1,pattern,patternP+1)
            return False                                                                                                                                    #如果字符串到头,模式串未匹配完毕，且无*,返回False，如('a','ab')
            
if __name__ == "__main__":
    print Solution().match('','')
                    
