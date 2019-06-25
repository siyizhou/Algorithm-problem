def merge_sort(l):
    if len(l) == 1:
        return l
    
    mid = len(l)//2
    left = l[:mid]
    right = l[mid:]
    
    l1 = merge_sort(left)
    l2 = merge_sort(right)
    
    return merge(l1,l2)

def merge(l1,l2):
    a1 = 0
    a2 = 0
    l = []
    while a1 < len(l1) and a2 < len(l2):
        if l1[a1]<l2[a2]:
            l.append(l1[a1])
            a1 += 1
        elif l1[a1]>l2[a2]:
            l.append(l2[a2])
            a2 += 1
        else:
            l.extend([l1[a1],l2[a2]])
            a1 += 1
            a2 += 1
    if a1 == len(l1):
        l.extend(l2[a2:])
    else:
        l.extend(l1[a1:])
    return l

l = [5,4 ,3 ,2 ,1]
merge_sort(l)
