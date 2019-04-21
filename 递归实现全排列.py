#输出一个数的全排列
#如：输入2，输出1，2 以及 2，1

#排列：从n个元素中任取m个元素，并按照一定的顺序进行排列，称为排列
#全排列：当n==m时，称为全排列

class perm:
    def perm_function(self,list1,s=""):
        if type(list1)!=type([]):
            return
        if len(list1)==0:  #参数合法性检验
            return
        if len(list1)==1:     #跳出条件
            print(s+list1[0])   #打印当前结果
            return 
        for i,e in enumerate(list1):
            self.perm_function(list1[:i]+list1[i+1:],s+e)
            
f=perm()
f.perm_function(["1","2","3"])
