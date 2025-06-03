K = int(input())
A, B = map(int, input().split())
XK = list(x * K for x in range(1, 1000//K + 1))
for i in XK:
    if (A <= i) & (i <= B):
        print('OK')
        break
else:
    print('NG')
