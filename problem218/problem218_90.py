import collections
N = int(input())
S = [input() for _ in range(N)]
c = collections.Counter(S)
d = c.most_common()
cnt = 0
for i in range(len(c)-1):
    if d[i][1] == d[i+1][1]:
        cnt += 1
    else:
        break
e = []
for j in range(cnt+1):
    e.append(d[j][0])
e.sort()
for k in range(len(e)):
    print(e[k])