def fun(l):
    if not l:
        return []
    
    for i in range(1,len(l),1):
        tmp = l[i]
        j = i-1
        while tmp < l[j] and j >= 0:
            l[j+1] = l[j]
            j = j-1
        l[j+1] = tmp
    return l
