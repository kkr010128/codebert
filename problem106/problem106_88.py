N = int(input())

ans = [0]*80100
for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            ans[x**2+y**2+z**2+x*y+y*z+z*x] += 1

for i in range(1, N+1):
    print(ans[i])
