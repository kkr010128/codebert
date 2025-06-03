r,c = map(int,input().split())

a = [list(map(int,input().split(" "))) for i in range(r)]

for i in range(r):
    r_total = sum(a[i])
    a[i].append(r_total)

c_total = []

for j in range(c+1):
    s = 0
    for k in range(r):
        s += a[k][j]
    c_total.append(s)

a.append(c_total)

for z in range(r+1):
    for w in range(c+1):
        print(a[z][w],end="")
        if w != c:
            print(" ",end="")
    print()