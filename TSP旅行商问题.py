import sys
n = int(sys.stdin.readline().strip())
m = []
for i in range(n):
    s = list(map(int,sys.stdin.readline().strip().split()))
    m.append(s)

# m = [[0, 2, 6, 5], [2, 0, 4, 4], [6, 4, 0, 2], [5, 4, 2, 0]]
n = len(m)
dp = [[float('inf') for i in range(2**(n-1))] for i in range(n)]

for i in range(n):
    dp[i][0] =  m[i][0]

for j in range(1,2**(n-1)):
    for i in range(n): 
        # dp[i][j]
        if  i!=0 and (j >> (i-1)) & 1:   # 如果i在j中,即换算成二进制以后，j的第i位为1。不合理，跳过
            continue
        for k in range(1,n):
            if not ((j >> (k-1)) & 1):  #如果j中的第k为0
                continue
            if dp[i][j] > m[i][k] + dp[k][j ^ (1<<(k-1))]:
                dp[i][j] = m[i][k] + dp[k][j ^ (1<<(k-1))]

print(dp[0][-1])


#  此代码算法复杂度过大，超时，未能运行完所有案例
