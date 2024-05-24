def recur(k):
    if (k==0):
        return k
    total = k + recur(k-1)
    print(total)
    return total
    
recur(6)