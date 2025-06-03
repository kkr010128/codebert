n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))
flag = [False] * 2000

for i in range(2 ** n):
    total = 0
    for j in range(n):
        if((i >> j) & 1):
            total += A[j]
    flag[total] = True
for m in M:
    print('yes' if flag[m] else 'no')
