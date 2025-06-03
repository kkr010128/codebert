import itertools,sys
def S(): return sys.stdin.readline().rstrip()
S = S()
groupby_S = itertools.groupby(S)
ans = 0
rangeN = [i for i in range(len(S)+1)]
rangeN_accumulate = list(itertools.accumulate(rangeN))
group = []
temp = []
for k,g in groupby_S:
    if k=='<':
        temp.append(len(list(g)))
    else:
        temp.append(len(list(g)))
        group.append(temp)
        temp = []
group.append(temp)
for x in group:
    if len(x)==0:
        continue
    elif len(x)==1:
        ans += rangeN_accumulate[x[0]]
    else:
        a,b = max(x),min(x)-1
        ans += rangeN_accumulate[a]
        ans += rangeN_accumulate[b]
print(ans)
