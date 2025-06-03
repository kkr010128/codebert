n,k = map(int,input().split())
a = list(map(int,input().split()))
si = [0 for i in range(n+1)]
p = [1 for i in range(n)]
import copy 
for q in range(min(k,50)):
    v = 0
    s = copy.deepcopy(si)
    for i in range(n):
        if a[i] != 0:
            s[max(i-a[i],0)] += 1
            s[min(i+a[i]+1,n)] -= 1
            a[i] = 0
        else:
            a[i] = 1
    for i in range(n):
        v += s[i]
        a[i] += v
for i in range(n):
    print(a[i], end = ' ')