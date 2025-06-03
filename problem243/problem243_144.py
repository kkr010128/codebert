n = int(input())
p = [input().split() for i in range(n)]
x = input()
ans = 0
f = False
for l in p:
    if f:
        ans+=int(l[1])
    if l[0]==x:
        f = True
print(ans)