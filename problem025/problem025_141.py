n = int(input())
A = list(map(int,input().split()))
q = int(input())
M = list(map(int,input().split()))

flag = [0]*(2000+1)
for status in range(2**n):
    tmp = 0
    for mask in range(n):
        if status&(1<<mask):
            tmp += A[mask]
    flag[tmp] = True

for m in M:
    print('yes' if flag[m] else 'no')
