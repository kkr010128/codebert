n = int(input())
a = list(map(int,input().split()))
m = 1000
stocks = 0
drops = [False]*(n-1)
for i in range(n-1):
    if a[i] > a[i+1]:
        drops[i] = True
for i in range(n-1):
    if drops[i]:
        m+=stocks*a[i]
        stocks = 0
    else:
        stocks+=m//a[i]
        m -= (m//a[i])*a[i]
print(m + stocks*a[-1])