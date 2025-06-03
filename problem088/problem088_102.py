N = int(input())
A = [int(x) for x in input().split()]
base = 0
diff = 0
for i in range(N):
    if A[i] > base:
        base = A[i]
    diff += base - A[i]
print(diff)
