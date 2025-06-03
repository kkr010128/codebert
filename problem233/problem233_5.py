N = int(input())
l = input().split()
p = []
for i in range(N):
    p.append((int(l[i]),i))

p.sort()

s = N
ans = 0
for i in range(N):
    (a,b) = p[i]
    if b < s:
        ans += 1
        s = b
print(ans)