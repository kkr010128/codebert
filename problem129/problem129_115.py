x = int(input())
p = sorted(list(map(int,input().split())))
d = [True]*(p[-1]+1)
e = [False]*(p[-1]+1)
for i in p:
    if e[i]:
        d[i] = False
        continue
    else:
        e[i] = True
    idx = 2*i
    while idx < len(d):
        d[idx] = False
        idx += i

cnt = 0
for i in p:
    cnt += int(d[i])    
print(cnt)