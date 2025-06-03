N = int(input())
ans = [0]*10010

for x in range(1, 105):
    for y in range(1, 105):
        for z in range(1, 105):
            v = x*x + y*y + z*z + x*y + y*z + z*x
            if v <= 10005:
                ans[v] += 1
for i in range(1, N+1):
    print(ans[i])