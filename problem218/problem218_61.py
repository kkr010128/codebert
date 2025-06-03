import collections

N = int(input())
S = [input() for i in range(N)]
C = collections.Counter(S)
L = C.most_common()

ans = []
flag = 0

for n in range(len(C)):
    if L[n][1] < flag:
        break
    else:
        ans.append(L[n][0])
        flag = (L[n][1])

ans.sort()

for i in range(len(ans)):
    print(ans[i])