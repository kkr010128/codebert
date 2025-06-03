r,c = map(int,raw_input().split())
a = [map(int,raw_input().split()) for _ in range(r)]
b = [0 for _ in range(c)]

for i in range(r) :
    s = 0
    for j in range(c) :
        s = s + a[i][j]
        b[j] = b[j] + a[i][j]
    a[i].append(s)
    print ' '.join(map(str,a[i]))
b.append(sum(b))
print ' '.join(map(str,b))