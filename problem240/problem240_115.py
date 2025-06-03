n,m = map(int,input().split())
a = [0]*n
ac =0
wa = 0

for i in range(m):
    p,s =  map(str,input().split())
    p = int(p)
    if s == "AC" and a[p-1] !=-1:
        ac +=1
        wa += a[p-1]
        a[p-1] = -1
    elif s =="WA" and a[p-1] != -1:
        a[p-1] += 1
print(ac,wa)