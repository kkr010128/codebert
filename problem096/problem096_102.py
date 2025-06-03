N, D = map(int, input().split())

X = [0] * N
Y = [0] * N

for i in range(N):
    X[i], Y[i] = map(int, input().split())

count = 0

for i in range(N):
    if(D**2 >= X[i]**2 + Y[i]**2):
        count += 1

print(count)
