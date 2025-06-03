n = int(input())
s = []
for i in range(n):
    a = input()
    b = []
    for j in range(len(a)):
        if a[j]=='(':
            b.append(1)
        else:
            b.append(-1)
    s.append(b)

l = []
r = []
for x in s:
    b = 0
    c = 0
    for y in x:
        c+=y
        b = min(b,c)
    z = len(x)
    d = 0
    e = 0
    for j in range(z):
        e += x[z-j-1]
        d = max(d,e)
    if c>0:
        l.append([b,c])
    else:
        r.append([d,c])
l.sort(reverse=True)
r.sort()

flag = 1
x = 0
for b,c in l:
    if x+b<0:
        flag = 0
    x += c

y = 0
for d,c in r:
    if y+d>0:
        flag = 0
    y += c

if y+x!=0:
    flag = 0
print('Yes' if flag else'No')





