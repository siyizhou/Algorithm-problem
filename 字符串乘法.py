# 输入两个字符串，输出他们的乘积，比如输入"12","2",输出"24"

class mul:
    def mul_string(self,a,b):
        n1=len(a)
        n2=len(b)
        t="0"
        if n1<=n2:   #保证a是位数较多的数 
            a,b=b,a
            n1,n2=n2,n1
        for i in range(n2-1,-1,-1):
            #b[i]*a
            c=""
            d=["0"]
            for j in range(n1-1,0,-1):
                temp=str(int(b[i])*int(a[j])+int(d[0]))
                if len(temp)==1:
                    c=temp+c
                    d.insert(0,"0")
                else:
                    c=temp[-1]+c
                    d.insert(0,temp[0])
            temp=str(int(b[i])*int(a[0])+int(d[0]))
            c=temp+c
            c=c+"0"*(n2-1-i)
            t=int(t)+int(c)
        return t
