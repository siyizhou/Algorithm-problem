def fun(l):
    if not l:
        return []
    if len(l) == 1:
        return l
    tmp = l[0]
    before = []
    after = []
    
    for i in range(1,len(l),1):
        if l[i] >= tmp:
            after.append(l[i])
        else:
            before.append(l[i])
    return fun(before) + [tmp] + fun(after)
