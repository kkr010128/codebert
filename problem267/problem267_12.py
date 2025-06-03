N = int(input())
S = input()
ans = 0
for i in range(1000):
    res = str(i).zfill(3)
    cnt = 0
    p = res[cnt]
    for s in S:
        if p == s:
            cnt += 1
            if cnt == 3:
                ans += 1
                break
            p = res[cnt]
print(ans)