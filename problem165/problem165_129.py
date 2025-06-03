# C - gacha

n = int(input())
s = []
c = 1

for i in range(n):
    s.append(input())

s.sort()

for j in range(1,n):
    if s[j-1] != s[j]:
        c += 1


print(c)
