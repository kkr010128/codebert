import collections

n = int(input())
A = list(map(int, input().split()))
q = int(input())

CNT = collections.Counter(A)
ANS = []
ans = sum(A)

for i in range(q):
    b, c = map(int, input().split())
    t = CNT[b]
    ans +=(c - b) * t
    ANS.append(ans)
    CNT[c] += t
    CNT[b] = 0

for i in ANS:
    print(i)