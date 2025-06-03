def ceil(n):
    if n%1000:
        return (1+n//1000)*1000
    else:
        return n
    
def debt(n):
    if n==0: return 100000
    return int(ceil(debt(n-1)*1.05))

print(debt(int(input())))

