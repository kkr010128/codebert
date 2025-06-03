h,w,k = map(int,input().split())
c = []
for i in range(0,h):
    c.append(input())
def white(c,r,co):
    count = 0
    for i in range(0,h):
        for j in range(0,w):
            if r[i] != 0 and co[j] != 0 and c[i][j] == "#":
                count += 1            
    return count
import itertools
listr = list(itertools.product([0,1],repeat = h))
listc = list(itertools.product([0,1],repeat = w))
ans = 0
for i in range(0,2**h):
    for j in range(0,2**w):
        if white(c,listr[i],listc[j]) == k:
            ans += 1
print(ans)