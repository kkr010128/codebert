H,W,M=map(int,input().split())
nh=[0]*H
nw=[0]*W
boms=set()
for _ in range(M):
    h,w=map(int,input().split())
    nh[h-1] += 1
    nw[w-1] += 1
    boms.add((h-1, w-1))

maxh = max(nh)
maxw = max(nw)

i_indexes=[]
for i in range(H):
    if nh[i] == maxh:
        i_indexes.append(i)
j_indexes=[]
for j in range(W):
    if nw[j] == maxw:
        j_indexes.append(j)

for i in i_indexes:
    for j in j_indexes:
        if (i,j) in boms:
            continue
        print(maxh + maxw)
        exit()
print(maxh + maxw - 1)