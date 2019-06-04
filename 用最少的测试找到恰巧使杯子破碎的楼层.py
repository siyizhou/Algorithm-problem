# 问题：https://blog.csdn.net/dazhi_100/article/details/7944014

# 一种杯子，若在第N层被摔破，则在任何比N高的楼层均会破； 若在第M层不破，则在任何比M低的楼层均不会破。
# 给你两个这样的杯子，让你在100层高的楼层中测试，要求用最少的测试次数找出恰巧会使杯子破碎的楼层。


# 水杯摔碎问题，有n个水杯和k层楼，求最少测试几次可以确定水杯刚好在哪一层楼摔碎。


# 解答过程：假设从x层楼开始扔为f(n,x)，如果水杯碎了,水杯数量－1,需要探测的楼层为x-1层，则为f(n-1,x-1)
# 如果没碎,水杯还是n个,需要探测k-x层，则为f(n,k-x)


n = 3
k = 10

def fun(n,k):
    f = [[0 for i in range(k+1)] for j in range(n+1)]      # n+1行k+1列的矩阵，fij表示：i个水杯，j层楼，最少的测试次数找出恰巧会使杯子破碎的楼层
    for i in range(k+1):
        f[0][i] = 0
        f[1][i] = i
    for i in range(2,n+1):
        f[i][0] = 0
    for i in range(2,n+1):
        for j in range(1,k+1):
            mins = float('inf')
            for e in range(1,j+1):
                mins = min(mins,1+ max(f[i][j-e],f[i-1][e-1]))    # 从第e层楼开始，如果有玻璃杯碎了，那么就是i-1个玻璃杯，e-1层楼，否则为i个玻璃杯，j-e层楼
            f[i][j] = mins
    return f
fun(n,k)
