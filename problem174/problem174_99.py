def gcd(x,y):
    while y>0:
        x,y = y,x%y
    return x
K = int(input())
cnt = 0
for a in range(1,K+1):
    for b in range(1,K+1):
        for c in range(1,K+1):
            x = a
            x = gcd(x,b)
            x = gcd(x,c)
            cnt += x
print(cnt)