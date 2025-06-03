n, m, l = map(int, input().split())
a = []
b = []
for i in range(n):
    a.append(list(map(int, input().split())))
for k in range(m): 
    b.append(list(map(int, input().split())))
for i in range(n):
    for s in range(l):
        c = 0
        for k in range(m):
            c = c + a[i][k] * b[k][s]
        if (s == l-1):
                print('{}'.format(c), end = '')
        else:
                print('{}'.format(c), end = ' ')
    print()
            
    
