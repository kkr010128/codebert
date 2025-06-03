N, K, C = map(int, input().split())
S = list(input())

l = [0] * N
r = [0] * N
cnt = 1
yutori = 10 ** 10
for i, s in enumerate(S):
    if s == "o" and yutori > C:
        l[i] = cnt
        yutori = 0
        cnt += 1
    yutori += 1

S.reverse()
yutori = 10 ** 10
cnt = K
for i, s in enumerate(S):
    if s == "o" and yutori > C:
        r[i] = cnt
        yutori = 0
        cnt -= 1
    yutori += 1

ans = set()
r.reverse()
for i in range(N):
    if l[i] == r[i] and l[i] > 0:
        ans.add(i+1)

print(*ans, sep="\n")
