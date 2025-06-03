from itertools import combinations
n,m,k = map(int,input().split())
mat = []
for _ in range(n):
    mat.append(list(input()))

def black(row,col):
    new = [mat[i] for i in range(n) if i not in row]
    if not new:return 0
    new = list(zip(*new))
    new = [new[i] for i in range(m) if i not in col]
    if not new:return 0
    return sum([i.count("#") for i in new])
ans = 0
rows = []
cols = []
for i in range(0,n+1):
    rows += list(combinations([i for i in range(n)],i))
for i in range(0,m+1):
    cols += list(combinations([i for i in range(m)],i))
#print(rows,cols)
for row in rows:
    for col in cols:
        if black(set(row),set(col))==k:
            #print(row,col)
            ans+=1
print(ans)

