n = int(input())
N = int(n/1.08)
for i in range(3):
    if int((N + i) * 1.08) == n:
        print(N+i)
        break
else:
    print(':(')