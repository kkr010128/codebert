n = int(input())
s = []
t = []
for i in range(n):
    a,b = input().split()
    s.append(a)
    t.append(int(b))
x = s.index(input())
ans = 0
for i in range(x+1,n):
    ans += t[i]
print(ans)