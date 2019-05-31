# 2.万万没想到之抓捕孔连顺
import sys
n,d = list(map(int,sys.stdin.readline().strip().split()))
s = sys.stdin.readline().strip().split()
s = list(map(int,s))

MOD = 99997867
dp = [0]*n
dp[2] = 1 if s[2]-s[0]<=d else 0

j = 0
for i in range(3,n):
    while j < i and s[i] - s[j] > d:
        j += 1
    c = i - j
    dp[i] = dp[i-1] + (int(c*(c-1)/2) if c >= 2 else 0)

print(dp[-1]%MOD)





# 3.胡牌问题(递归）
import sys
s = list(map(int,sys.stdin.readline().strip().split()))

def hupai(s):
    if not s:
        return True
    count0 = s.count(s[0])
    if len(s)%3 !=0 and count0>=2 and hupai(s[2:]) == True:
        return True
    if count0>=3 and hupai(s[3:]) == True:
        return True
    if s[0]+1 in s and s[0]+2 in s:
        last_s = s.copy()
        last_s.remove(s[0])
        last_s.remove(s[0]+1)
        last_s.remove(s[0]+2)
        if hupai(last_s) == True:
            return True
    return False
  
t = []
for i in range(1,10):
    if s.count(i)<4:
        c = s.copy()
        c.append(i)
        c.sort()
        if hupai(c):
            t.append(i)
print(' '.join(map(str,t)))






# 4.猫咪特征提取
import sys
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

c = set()
d = dict()
for i in range(m):
    s = list(map(int,sys.stdin.readline().strip().split()))
    s_n  = s[0]
    s.pop(0)
    s_f = [(s[i],s[i+1]) for i in range(len(s)) if i%2==0]
    c.update(s_f)
    for j in s_f:
        if j not in d:
            d[j]=[]
        d[j].append(i)

def fun(s):
    f = 1
    a = 1
    if  len(s) == 1:
        return 1
    if len(s) == 2:
        if s[1]-s[0]==1:
            return 2
        else:
            return 1
    for i in range(len(s)-1):
        if s[i+1]-s[i] == 1:
            a += 1
        else:
            f = max(a,f)
            a = 1
    return max(a,f)    
    
l = list(d.keys())
r = []

for i in l:
    v = d[i]
    r.append(fun(v))
print(max(r))





# 5.毕业旅行问题（动态规划算法）
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





# 6.找零钱问题
import sys
n=int(sys.stdin.readline().strip())

s=1024-n

n1 = s//64
r1 = s%64
n2 = r1//16
r2 = r1%16
n3 = r2//4
r3 = r2%4
print(n1+n2+n3+r3)





# 7.机器人跳跃问题----二分法
import sys
n = int(sys.stdin.readline().strip())
h = list(map(int,sys.stdin.readline().strip().split()))

def fun(e):
    for i in range(n):
        if h[i] > e:
            e -= h[i]-e
        else:
            e += e-h[i]
        if e<0:
            return False
    return True

left,right = 0,max(h)

while right - left > 1:
    mid = (left + right) // 2
    if fun(mid):
        right = mid
    else:
        left = mid

if fun(left):
    print(left)
else:
    print(right)
