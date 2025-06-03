N = int(input())

ans = [0 for _ in range(N+1)]
for x in range(1, 101):
    for y in range(x, 101):
        for z in range(y, 101):
            v = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x
            if v < N+1:
                if x == y == z:
                    ans[v] += 1
                elif x == y or x == z or z == y:
                    ans[v] += 3
                else:
                    ans[v] += 6
for i in range(1,N+1):
    print(ans[i])
