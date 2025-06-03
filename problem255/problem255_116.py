n = int(input())
s, t = map(str, input().split())
sl = list(s)
tl = list(t)
a = []
for i in range(n):
    a.append(s[i])
    a.append(t[i])
print(''.join(a))