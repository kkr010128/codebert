n = int(input())
s, t = [], []
for i in range(n):
    si, ti = input().split()
    ti = int(ti)
    s.append(si)
    t.append(ti)
x = input()

bit = 0
ans = 0
for i in range(n):
    if s[i] == x:
        bit = 1
    else:
        if bit == 1:
            ans += t[i]

print(ans)