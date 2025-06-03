n = int(input())
s, t = input().split()

a = []
for i in range(n):
    a.append(s[i])
    a.append(t[i])
print(''.join(a))
