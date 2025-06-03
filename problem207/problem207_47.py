a = []
a1 = []
for i in range(3):
    a2 = list(map(int, input().split()))
    a.append(a2)
    a1 += a2
n = int(input())
b = []
num = 0
for h in range(n):
    b1 = int(input())
    if b1 in a1:
        num += 1
    b.append(b1)
if num < 3:
    print('No')
else:
    z = 'No'
    for j in range(3):
        if a[j][0] in b and a[j][1] in b and a[j][2] in b:
            z = 'Yes'
            break
        if a[0][j] in b and a[1][j] in b and a[2][j] in b:
            z = 'Yes'
            break
    if z == 'No':
        if a[0][0] in b and a[1][1] in b and a[2][2] in b:
            z = 'Yes'
        elif a[2][0] in b and a[1][1] in b and a[0][2] in b:
            z = 'Yes'
    print(z)