import collections
N = int(input())
S = [input() for i in range(N)]
S = sorted(S)


C = collections.Counter(S)

M = C.most_common()
V = C.values()
MAX = max(V)

for i in range(len(M)):
    if M[i][1] == MAX:
        print(M[i][0])
