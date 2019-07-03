#方法一：维护两个栈
#模拟将n个'('和n个')'分别放入两个栈中left和right。每次从两个栈中取值。
#如果left==right，此时我们只能从left中出栈
#如果left<right，那么就有两种选择，要么从left中出栈，要么充right中出栈。
#整个过程，要保证left<=right

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        
        res = []
        def fun(s,left,right):
            if left == 0 and right == 0:
                res.append(s)
                return
            
            if left == right:
                fun(s+'(',left-1,right)
            elif left < right:
                if left>=1:
                    fun(s+'(',left-1,right)
                if right>=1:
                    fun(s+')',left,right-1)
            else:
                return
            
        fun('',n,n)
        
        return res
            
        
        
