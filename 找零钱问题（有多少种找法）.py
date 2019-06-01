# 顾客们买完东西付款后，我们都要找零给他们，我们这边所有的硬币（1,3,4）都是充足的
# 我想知道一共有多少种找零方式？
# 递归 
def fun(x):
    if x == 0:
        return 1
    if x == 1:
        return 1
    if x == 2:
        return 1
    if x == 3:
        return 2
    return fun(x-1)+fun(x-3)+fun(x-4)
fun(4)
fun(40)


# 动态规划的方法，实际上把结果保存起来，牺牲一点内存空间，但速度会提升很多
def fun(n):
    if n <=2 :
        return 1
    if n == 3:
        return 2
    
    s = [0]*(n+1)
    s[0] = s[1] = s[2] = 1
    s[3] = 2 

    for i in range(4,n+1):
        s[i] = s[i-1]+s[i-3]+s[i-4]
    return s[n]
fun(40)


###
def fun(n):
    if n <= 2:
        return 1
    if n == 3:
        return 2
    
    s_0 = 1
    s_1 = 1
    s_2 = 1
    s_3 = 2
    
    for i in range(4,n+1):
        ans  = s_0 + s_1 + s_3
        s_0 = s_1
        s_1 = s_2
        s_2 = s_3
        s_3 = ans
    return ans
fun(40)
