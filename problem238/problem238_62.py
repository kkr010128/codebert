n , k , s = map(int,input().split())
l = []
for i in range(k):
    l.append(s)
if s == 1:
    t = 3
elif s == 10**9:
    t = 1
else:
    t = s + 1

for i in range(n-k):
    l.append(t)


print(' '.join(map(str, l)))