import numpy as np 

#定义重量
weight={}
weight["water"]=3
weight["book"]=1
weight["food"]=2
weight["jacket"]=2
weight["camera"]=1

#定义价值
worth={}
worth["water"]=10
worth["book"]=3
worth["food"]=9
worth["jacket"]=5
worth["camera"]=6 

#存放行标对应的物品名:
table_name={}
table_name[0]="water"
table_name[1]="book"
table_name[2]="food"
table_name[3]="jacket"
table_name[4]="camera"


#创建矩阵,用来保存价值表
table=np.zeros((len(weight),7))   # 0kg,1kg,2kg,...,6kg
table_things = [[[] for j in range(7)] for i in range(len(weight))] 

for i in range(0,len(weight)):    # table[i][j]
    for j in range(1,7):              
        this_weight = weight[table_name[i]]              
        this_worth = worth[table_name[i]]      
        tmp = 0
        
        if i > 0:
            before_worth = table[i-1][j]    # table[i-1][j], this_worth + table[i-1][j-this_weight]进行比较
            if j - this_weight >= 0:
                tmp = table[i-1][j - this_weight]
                table[i][j] = max(before_worth,tmp + this_worth)
                if table[i][j] == before_worth:
                    table_things[i][j] = table_things[i-1][j]
                else:
                    table_things[i][j] = table_things[i-1][j - this_weight]+[table_name[i]]
            else:
                table[i][j] = before_worth
                table_things[i][j] = table_things[i-1][j]
        else:
            if this_weight <= j:
                table[i][j] = this_worth
                table_things[i][j].append(table_name[i])
table
table_things
