N = int(input())

for X in range(1, N+1):
    if X*108//100==N:
        print(X)
        break
else:
    print(':(')