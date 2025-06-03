h,w,k = map(int, input().split())
ls = [list(input()) for i in range(h)]
ansls = [[0]*w for _ in range(h)]
absent = []
idx = 1
for i in range(h):
    if ls[i] == ['.']*w:
        absent.append(i)
    else:
        count=0
        for j in range(w):
            if ls[i][j] == "#":
                if count>0:
                    idx+=1
                count+=1
            ansls[i][j] = idx
        idx+=1

for i in absent:
    idx = i
    while idx in absent:
        idx+=1
    if idx>=h:
        idx = i
        while idx in absent:
            idx-=1
    ansls[i] = ansls[idx]

for l in ansls:
    print(*l)