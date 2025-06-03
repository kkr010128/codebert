import itertools
n = int(input())
A = list(map(int,input().split()))
q = int(input())
M = list(map(int,input().split()))

dp = []
for i in itertools.product([0, 1], repeat=n):
    tmp = 0
    for j in range(n):
        tmp += A[j] * i[j]
    dp.append(tmp)

for i in M:
    if i in dp:
        print('yes')
    else:print('no')
