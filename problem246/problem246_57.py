import itertools

n = int(input())
p = list(map(int, input().split()))
q = tuple(map(int, input().split()))
srt = sorted(p.copy())
cnt = 1
cnt1 = 0
cnt2 = 0
for i in itertools.permutations(srt, n):
    if i == tuple(p):
        cnt1 = cnt
    if i == q:
        cnt2 = cnt
    cnt += 1
print(abs(cnt1 - cnt2))