# 已知n个正数：wi, 1<=i<=n, 和M。要求找出{wi }的所有子集使得子集内元素之和等于M。
# 例如： n=4, (w1,w2,w3,w4)=(11,13,24,7)，M=31 则满足要求的子集是(11,13,7)和（24,7）

# 在此假设已将集合s处理成数列s,并且按由小到大的顺序排列

s = [7,11,13,24]
m = 31
n = 4

# 判断是否存在这样的子集
def fun(s,n,m):
    f = [[False for j in range(m+1)] for i in range(n+1)]   # n+1行，m+1列
    for i in range(n+1):
        f[i][0] = True
    for i in range(1,m+1):
        f[0][i] = False
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s[i-1] > m:
                f[i][j] = f[i-1][j]
            else:
                f[i][j] = f[i-1][j] or f[i-1][j-s[i-1]]
    return f
f = fun(s,n,m)
f[n][m]

# 找到一个这样的子集
result = []
if f[n][m]:
    i = n
    for i in range(n,0,-1):
        if f[i][m] and (not f[i-1][m]):
            result.append(s[i-1])
            m = m - s[i-1]
        if m <= 0:
            break
