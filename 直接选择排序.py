def fun(l):
    if l == []:
        return []
    for i in range(len(l)-1):
        min = i
        for j in range(i,len(l),1):
            if l[j] < l[min]:
                min = j
        if min != i:
            l[i],l[min] = l[min],l[i]
    return l
