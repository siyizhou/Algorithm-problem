def fun1(l):
    if l == []:
        return []
    
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l
  
  
  
  def fun(l):
    if l == []:
        return []
    
    s = []
    while l:
        n = len(l)
        for i in range(n-1):
            if l[i] > l[i+1]:
                l[i],l[i+1] =  l[i+1],l[i]
        a = l.pop()
        s.insert(0,a)
    
    return s
