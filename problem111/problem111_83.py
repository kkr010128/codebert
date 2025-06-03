n = int(input())
ls = list(map(int,input().split()))
ls.sort(reverse=True)
p = len(ls)
if len(ls)%2 == 1:
    p += 1
p //= 2
q = 0
for i in range(1,p+1):
    if i == 1:
        q += ls[0]
    else:
        if i == p:
            if len(ls)%2 == 1:
                q += ls[p-1]
            else:
                q += 2*ls[p-1]
        else:
            q += 2*ls[i-1]
print(q)