n = input()
n = n.split()
m = int(n[1])
n = int(n[0])
a = input()
a = a.split()
c = int(a[0])
for b in range(n-1):
    c = c + int(a[b+1])
c = c / (4 * m)
e = 0
for d in range(n):
    if int(a[d]) >= c :
        e = e + 1
if e >= m:
    print("Yes")
else:
    print("No")