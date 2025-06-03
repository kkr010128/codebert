N, D = map(int, input().split())
x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = map(int, input().split())


c = 0
for j in range(N):
    if x[j]**2 + y[j]**2 <= D**2:
        c += 1

print(c)