a = list(map(int,input().split()))
b = [0, 0, 0, 0]

b[0] = a[0]*a[2]
b[1] = a[0]*a[3]
b[2] = a[1]*a[2]
b[3] = a[1]*a[3]

b.sort()

print(b[3])