n = int(input())
ss = []
tt = []
for _ in range(n):
    s,t = input().split()
    ss.append(s)
    tt.append(int(t))
x = input()

for i in range(n):
    if ss[i] == x:
        ans = sum(tt[i+1:])
        break

print(ans)