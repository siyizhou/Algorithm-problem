# 出售价格
p={1:2,2:5,3:8,4:9,5:10,6:17,7:17,8:20,9:24,10:30}
n = 9

k = list(p.keys())

def fun(k,n):
    v = [0 for i in range(n+1)]
    g = [[] for i in range(n+1)]
    for i in range(1,n+1):
        s = []
        for j in k:
            if i>=j:
                s.append(p[j]+v[i-j])
        v[i] = max(s)
        index = s.index(max(s))
        g[i] = [index+1] + g[i-index-1]
        
    return v,g
    
fun(k,9)
# 返回最大的价值，以及最大价值对应的切割方案

# 想法：建立一个n+1维的向量分别表示idx+1长的钢条所对应的切割后的最大价值

