N, M = map(int, input().split())
A = list(map(int, input().split()))

if N - sum(A) <= 0:
    result = "Yes"
else:
    result = "No"
print(result)