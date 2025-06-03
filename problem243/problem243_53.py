n = int(input())
s, t = [], []
for i in range(n):
    ss = input().split()
    s.append(ss[0])
    t.append(int(ss[1]))
x = input()
start = n
for i in range(n):
    if s[i] == x:
        start = i + 1
res = 0
for i in range(start, n):
    res += t[i]
print(res)