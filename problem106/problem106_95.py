N = int(input())

ans = [0 for i in range(10**4+1)]
for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            n = x*x + y*y + z*z + x*y + y*z + z*x
            if n <= 10**4:
                ans[n] += 1

for i in range(1, N+1):
    print(ans[i])