N = int(input())
A = list(map(int, input().split()))
fumidai = 0
previous = 0
for i in range(N):
    if previous > A[i]:
        fumidai += previous - A[i]
    else:
        previous = A[i]
        continue
print(fumidai)