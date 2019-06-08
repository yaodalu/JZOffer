# -*- coding:utf-8 -*-
import re

class Solution:
    # s字符串
    def isNumeric(self, s):
        """正则版本"""
        pattern1 = re.compile(r'([+-]?[1-9]+|0)')                                                                           #自然数
        pattern2 = re.compile(r'[+-]?[0-9]+[\\.][0-9]+')                                                                    #浮点数
        pattern3 = re.compile(r'[+-]?[1-9]+[e|E][-]?[1-9]+')                                                                #自然数为底数的科学计数法
        pattern4 = re.compile(r'[+-]?[0-9]+[\\.][0-9]+[e|E][-]?[1-9]+')                                                     #浮点数为底数的科学计数法
        return pattern1.match(s) == [] or pattern2.match(s) == [] or pattern3.match(s) == [] or pattern4.match(s) == []

    def isNumeric1(self,s):
        """遍历版本"""
        if s[0] == '+' or s[0] == '-':
            return self.isExponent(s[1:].upper())                                                                           #去掉符号,统一大写
        return self.isExponent(s.upper())

    def isExponent(self,s):
        """判断是否是科学记数法形式"""
        if s.find('E') == -1 :
            return self.isInteger(s) or self.isFloat(s)                                                                     
        else:                                                                                                               #科学记数法表示
            base = s.split('E')[0]
            exp = s[len(base)+1:]
            if bool(base) and bool(exp):
                if exp[0] == '+' or exp[0] == '-':
                    return (self.isInteger(base) or self.isFloat(base)) and self.isInteger(exp[1:])
                return (self.isInteger(base) or self.isFloat(base)) and self.isInteger(exp)
            else:
                return False

    def isFloat(self,s):
        """判断是否是浮点数"""
        p1 = s.split('.')[0]
        p2 = s[len(p1)+1:]
        if p1:                                                                                                              #如果含小数点                                                                                                            
            return bool(p2) and self.isInteger(p1) and self.isInteger(p2)
        else:
            return bool(p2) and self.isInteger(p2)                                                                           
        
    def isInteger(self,s):
        """判断整数是否合法"""
        return s == '0' or (s[0] != '0' and s.isdigit())

if __name__ == "__main__":
    solution = Solution()
    """合法字符串"""
    print solution.isNumeric1('12')                                                                                       
    print solution.isNumeric1('-12.4')
    print solution.isNumeric1('12e2')
    print solution.isNumeric1('-12.2e-9')
    print solution.isNumeric1('-.123')
    print solution.isNumeric1('2e+10')

    """不合法字符串"""
    print solution.isNumeric1('1a3.14')
    print solution.isNumeric1('12e')                                                                                      
    print solution.isNumeric1('1.2.3')
    print solution.isNumeric1('+-5')
    print solution.isNumeric1('12e4.3')



