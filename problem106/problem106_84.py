N = int(input())

MX = 10**4
ans = {}
for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            tmp = x**2+y**2+z**2+x*y+x*z+y*z
            if tmp > MX:
                break
            if not(tmp in ans):
                ans[tmp] = 1
            else:
                ans[tmp] += 1

for i in range(1, N+1):
    if i in ans:
        print(ans[i])
    else:
        print(0)
