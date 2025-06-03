n = int(input())
A = list(map(int, input().split()))
a_sum = 0
for i in A:
    a_sum ^= i
for i in range(n):
    A[i] ^= a_sum
print(*A)