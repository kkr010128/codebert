def divisor(x):
    table = []
    i = 1
    while i * i <= x:
        if x%i == 0:
            table.append(i)
            table.append(n//i)
        
        i +=1
        
    table.sort()
    return table 
    
n = int(input())

l = divisor(n)
c = len(l)

ans = 100100100100100
for i in range(c):
    x = l[i] - 1
    y = l[c-i-1] - 1
    tot = x + y
    ans = min(ans,tot)
    
print(ans)