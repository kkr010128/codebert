N = int(input())
A = list(map(int, input().split()))

res = 0
for i in range(1, N + 1):
    if i % 2 == 1 and A[i-1] % 2 == 1:
       res += 1

print(res)
