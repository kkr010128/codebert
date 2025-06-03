n, k = map(int, input().split())

su = 0
for i in range(k, n+2):
    co = (n+(n-i+1))*i/2 - (i-1)*i/2 + 1
    su = (su + int(co)) % (10**9 + 7)
    
print(su)