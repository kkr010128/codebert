n = int(input())
a = list(map(int, input().split()))

A = max(a)

cnt = [0]*(A+1)
uq = []

for i in a:
    cnt[i] += 1

for i in range(A+1):
    if cnt[i] == 1:
        uq.append(i)

cnt = [0]*((10**6)+1)
cnt1 = 0


a = list(set(a))

# for i in a:
#     for j in range(2,A+1):
#         if i*j<=A+1:
#             cnt[i*j] = 1

for elem in a:
    for m in range(elem * 2, (10 ** 6) + 1, elem):
        cnt[m] = 1

for i in uq:
    if cnt[i] == 0:
        cnt1 += 1

print(cnt1)
