# 实现两个字符串的加法，比如输入"13"，"13"，返回"26"

class add:
    def add_string(self,a,b):
        n1=len(a)
        n2=len(b)
        if n1>=n2:    # 将数据补齐
            b="0"*(n1-n2)+b
        else:
            a="0"*(n2-n1)+a
        n=max(n1,n2)
        c=d=[0]*n    
        for i in range(n-1,-1,-1):
            if int(a[i])+int(b[i])<10:
                c[i]=str(int(a[i])+int(b[i])+int(d[i]))
            else:
                c[i]=str(int(a[i])+int(b[i])+int(d[i])-10)
                d[i-1]=d[i-1]+1
        return "".join(c)    
 
#注意：两个字符串s1,s2，s1+s2是将两个字符串连接起来，成为一个新的字符串
#因此，c[i]=str(int(a[i])+int(b[i])+int(d[i]))，要在提取出来的字符前加一个int函数，以便进行加法运算
#S.join(c) :将序列对象中所有所有的字符串合并成为一个字符串，S对象为连接分隔符
