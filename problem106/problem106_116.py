N = int(input())
ans = [0]*10050

for i in range(N+1):
    ans.append(0)

for x in range(1,105):
    for y in range(1,105):
        for z in range(1,105):
            tmp = x**2 + y**2 + z**2 + x*y + y*z + z*x
            if tmp < 10050:
                ans[tmp] += 1
for i in range(N):
    print(ans[i+1])