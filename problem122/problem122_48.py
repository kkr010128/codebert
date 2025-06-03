n = int(input())
a = list(map(int, input().split()))
q = int(input())
sm = sum(a)
hm = [0] * (10 ** 5 + 1)
for i in a:
    hm[i] += 1
for _ in range(q):
    b, c = map(int, input().split())
    sm += (c - b) * hm[b]
    hm[c] += hm[b]
    hm[b] = 0
    print(sm)