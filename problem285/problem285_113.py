s = input()
n = len(s) + 1

A = [0] * n
for i in range(1, n):
    if s[i - 1] == "<":
        A[i] = A[i - 1] + 1

for i in range(n - 1, 0, -1):
    if s[i - 1] == ">":
        A[i - 1] = max(A[i - 1], A[i] + 1)

print(sum(A))
