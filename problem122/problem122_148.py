'''
参考
https://drken1215.hatenablog.com/entry/2020/06/21/224900
'''
N = int(input())
A = list(map(int, input().split()))

INF = 10 ** 5
cnt = [0] * (INF+1)

Q = int(input())
BC = []

for _ in range(Q):
    BC.append(list(map(int, input().split())))

for a in A:
    cnt[a] += 1

total = sum(A)

for b, c in BC:
    total += (c-b) * cnt[b]
    cnt[c] += cnt[b]
    cnt[b] = 0
    print(total)
