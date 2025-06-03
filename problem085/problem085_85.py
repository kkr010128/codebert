N = int(input())
A = list(map(int, input().split()))

cnt = [0] * (10**6 + 1)
for i in range(N):
    cnt[A[i]] += 1

flag = True
for i in range(2, 10**6 + 1):
    multiple = 0
    for j in range(i, 10**6 + 1, i):
        multiple += cnt[j]
    if multiple == N:
        print("not coprime")
        exit()
    if multiple >= 2:
        flag = False

print("pairwise coprime" if flag else "setwise coprime")
