N = int(input())
lis = [0]*N
for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            ans = x**2 + y**2 + z**2 + x*y + y*z + z*x -1
            if ans >= N:
                pass
            else:
                lis[ans] += 1
for i in range(N):
    print(lis[i])