N = int(input())

ans = [0 for _ in range(10050)]

for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            a = x**2 + y**2 + z**2 + x*y + y*z + z*x
            if a < 10050:
                ans[a] += 1
for i in range(1,N+1):
    print(ans[i])
