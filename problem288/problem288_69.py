from itertools import product
n = int(input())

ans = n-1
for a in range(1, int(n**0.5)+1):
    if n%a==0:
        b = n//a
        ans = min(ans, b+a-2)
print(ans)