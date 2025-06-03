import collections

n = int(input())
a = list(map(int, input().split()))
q = int(input())

bc = []

for i in range(q):
    bci = list(map(int, input().split()))
    bc.append(bci)

d = collections.Counter(a)
ans = sum(a)

for i in range(q):
    b, c = bc[i]
    num = (c-b)*d[b]
    ans += num
    print(ans)
    d[c] += d[b]
    d[b] = 0