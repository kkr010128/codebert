n = int(input())
fo_x = '0' + str(n) + 'b'
a = [None] * n
x = [None] * n
y = [None] * n
ans = 0
flag = 0
for i in range(n):
    a[i] = int(input())
    ax = [None] * a[i]
    ay = [None] * a[i]
    for j in range(a[i]):
        ax[j],ay[j] = map(int,input().split())
    x[i] = ax
    y[i] = ay

for i in range(2 ** n):
    b = format(i,fo_x)
    for j in range(len(b)):
        if b[j] == '0':
            continue
        for z in range(a[j]):
            if str(y[j][z]) != b[x[j][z]-1]:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 0:
        ans = max(ans,b.count('1'))
    flag = 0
print(ans)