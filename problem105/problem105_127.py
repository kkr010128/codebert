N = int(input())
A = list([int(x) for x in input().split()])

count = 0
for i in range(0, N, 2):
    if A[i] % 2 == 1:
        count += 1

print(count)
