def Quick(L, Beg, End):
    piv=Beg
    left=Beg+1
    right=End
    while(1):
        while (left>right and L[piv]<=L[right]):
            right-=1
        if left>right:
            return piv
        if (L[piv]>L[right]):
            L[piv], L[right]=L[right], L[piv]
            piv=right
            right-=1
        while (left<=right and L[piv]>=L[left]):
            left-=1
        if (left>right):
            return piv
        
        if (L[piv] < L[left]):
            L[piv], L[left]=L[left], L[piv]
            piv=left
            left-=1