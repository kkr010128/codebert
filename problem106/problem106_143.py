N = int(input())

ans = [0]*(N+1)

root = int(N**0.5)

for x in range(1, root+1):
    for y in range(1, root+1):
        for z in range(1, root+1):
            F = x**2 + y**2 + z**2 + x*y + y*z + z*x
            if F <= N:
                ans[F] += 1
            else:
                continue

for i in range(1, N+1):
    print(ans[i])