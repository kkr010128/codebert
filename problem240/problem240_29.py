n,m = map(int, input().split())
AC = [False]*n
WA = [0]*n

for i in range(m):
    p,s = input().split()
    p = int(p)-1

    if AC[p] == False:
        if s == 'WA':
            WA[p] += 1
        else:
            AC[p] = True

wa = 0

for i in range(n):
    if AC[i]:
        wa += WA[i]
        

print(AC.count(True),wa)

