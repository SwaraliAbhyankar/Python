def minimum(*val, low_limit=None):
    if low_limit is None:
        return min(val)
    else: 
        L = [x for x in val if x >= low_limit]
        return min(L)

print(minimum(1, -3, 2, -4, 6, low_limit=0))