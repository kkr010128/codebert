N = int(input())
ans = [0]*(N+1)
for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            num = x*x + y*y + z*z + x*y + y*z + z*x
            if num>N:
                break
            ans[num] = ans[num] + 1
for m in ans[1:]:
    print(m)
