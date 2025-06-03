v = 0
i = 0
a = []
while v == 0:
    x = input()
    if 0 == int(x):
        v = 1
    else:
        a.append(int(x))
        i = int(i) + 1

for j in range(int(i)):
    print('Case %d: %d' % (int(j)+1,a[int(j)] ))
