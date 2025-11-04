L = [5,7,3,2,6,1,5,9]

def reverse(L, left, right):
    if left >= right:
        return
    
    L[left], L[right] = L[right], L[left]
    reverse(L, left+1, right-1)

reverse(L,0,8)