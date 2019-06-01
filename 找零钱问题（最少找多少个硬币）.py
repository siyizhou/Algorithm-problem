def fun(n):
    s  = [0]*(n+1)
    r = [[] for i in range(n+1)]
    s[1] = 1
    s[2] = 2
    s[3] = 1
    s[4] = 1
    r[1] = [1]
    r[2] = [1,1]
    r[3] = [3]
    r[4] = [4]
    
    for i in range(5,n+1):
        s_1 = 1 + s[i-1]
        s_3 = 1 + s[i-3]
        s_4 = 1 + s[i-4]
        s[i] = min(s_1,s_3,s_4)
        if s[i] == s_1:
            r[i] = [1] + r[i-1]
        if s[i] == s_3:
            r[i] = [3] + r[i-3]
        if s[i] == s_4:
            r[i] = [4] + r[i-4]
    return s[n],r[n]
    
a,b=fun(50)
# b为对应的找法
