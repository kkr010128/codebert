n=int(input())
c= sorted(list(map(int, input().split())), reverse=True)
l = len(c)
m = l//2
ans = c[0]

if l%2 == 0:
    for i in range(1,m):
        ans += 2*c[i]
else:
    for i in range(1,m):
        ans += 2*c[i]
    ans += c[m]
print(ans)