A:0, 0
B:M-1,N-1

-------------
| A | 0 | 1 |
-------------
| 1 | 1 | 0 |
-------------
| 1 | 0 | B |
-------------


目标：A -> B
限制：每一步只能往下或者往右，1-可以走，0--不能走
问题：有多少种走法
输入：M * N  -- 0 1 矩阵


# 穷举
class Solution():
    def findnums(self,m):
        r = len(m)
        c = len(m[0])
        
        n = 0
        def helper(m,a,b):
            if a == r-1 and b == c-1:
                n += 1
                return 
            if b == c-1:
                if m[a+1][b] == 1:
                    helper(m,a+1,b)
                else:
                    return
            if m[a][b+1] == 1:
                helper(m,a,b+1)
            if a == r-1:
                if m[a][b+1] == 1：
                    helper(m,a,b+1)
                else:
                    reutrn
            if m[a+1][b] == 1:
                helper(m,a+1,b)
            
        helper(m,0,0)
        return n
        
        
        
        
# 动态规划：时间复杂度MN
class Solution():
    def findway(self,m):
        r = len(m)
        c = len(m[0])
        
        if r == 0 or c == 0:
            return 0
        
        
        res = [[0 for j in range(c)] for i in range(r)]
        
        res[0][0] = 1
        
        for i in range(1,c):
            if m[0][i] == 1:
                res[0][i] = res[0][i-1]
            else:
                break
        
        for i in range(1,r):
            if m[i][0] == 1:
                res[i][0] = res[i-1][0]
            else:
                break
                
            
        
        for i in range(1,r):
            for j in range(1,c):
                if m[i][j] == 1:
                    res[i][j] = res[i-1][j] + res[i][j-1]
                
        return res[-1][-1] 
        
   c = Solution()
   c.findway([[1,0,1],[1,1,0],[1,1,1]])

