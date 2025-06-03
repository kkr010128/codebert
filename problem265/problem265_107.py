N = int(input())

for x in range(N+1):
    if int(x*1.08) == N:
        print(x)
        break
else:
    print(':(')