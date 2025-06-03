N = int(input())


for i in range(N+1):
    X = i * 1.08
    if int(X) == N:
        print(i)
        exit()

print(':(')