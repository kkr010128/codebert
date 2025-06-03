n = int(input())
s = []
t = []
for i in range(n):
    s_, t_ = map(str, input().split())
    s.append(s_)
    t.append(int(t_))
x = input()

for i in range(n):
    if s[i] == x:
        break

ans = 0
for j in range(n-1, i, -1):
    ans += t[j]
print(ans)