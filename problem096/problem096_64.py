N, D = map(int, input().split())
result = 0
for i in range(N):
    a, b = map(int, input().split())
    if a**2 + b**2 <= D**2:
        result += 1
print(result)