n = int(input())
a = int(n**0.5+1)
ans = [0]*n
for x in range(1, a):
    for y in range(1, a):
        for z in range(1, a):
            if x**2 + y**2 + z**2 + x*y + y*z + z*x <= n:
                ans[x**2 + y**2 + z**2 + x*y + y*z + z*x -1] += 1
[print(i) for i in ans]