x = list(map(int,input().split()))
y = list(map(int,input().split()))
z = list(map(int,input().split()))
n = int(input())
for i in range(n):
    b = int(input())
    if b in x:
        x[x.index(b)] = 'T'
    if b in y:
        y[y.index(b)] = 'T'
    if b in z:
        z[z.index(b)] = 'T'
if x[0] == 'T' and x[1] == 'T' and x[2] == 'T':
    print('Yes')
elif y[0] == 'T' and y[1] == 'T' and y[2] == 'T':
    print('Yes')
elif z[0] == 'T' and z[1] == 'T' and z[2] == 'T':
    print('Yes')
elif x[0] == 'T' and y[0] == 'T' and z[0] == 'T':
    print('Yes')
elif x[1] == 'T' and y[1] == 'T' and z[1] == 'T':
    print('Yes')
elif x[2] == 'T' and y[2] == 'T' and z[2] == 'T':
    print('Yes')
elif x[0] == 'T' and y[1] == 'T' and z[2] == 'T':
    print('Yes')
elif x[2] == 'T' and y[1] == 'T' and z[0] == 'T':
    print('Yes')
else:
    print('No')