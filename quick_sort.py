def Quick_sort(list):
    if len(list)<=1:
        return list
    else:
        pivot=list[0]
        
        left=[x for x in list[1:] if x<=pivot]
        right=[x for x in list[1:] if x>pivot]
        
        return Quick_sort(left)+[pivot]+Quick_sort(right)
        
list1=[64,35,89,64,21,72,32]
l=Quick_sort(list1)
print(l)