n = int(input())
s = []
t = []
for i in range(n):
    ss,tt = map(str,input().split())
    s.append(ss)
    t.append(tt)
x = input()

ans = 0
for i in range(n-1):
    if ans != 0:
        ans += int(t[i+1])
    elif s[i] == x:
        ans += int(t[i+1])
print(ans)