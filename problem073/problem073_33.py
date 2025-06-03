n = int(input())
ans = 0
for a in range(1, n+1):
    b=1
    while n-a*b>0:
        ans += 1
        b+=1
print(ans)
