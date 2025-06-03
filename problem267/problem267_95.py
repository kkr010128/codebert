n = int(input())
S = input()
ans = 0
nums = list(map(str, range(10)))
for i in nums:
    s1 = S.find(i)
    if s1 < 0:
        continue
    for j in nums:
        s2 = S.find(j, s1+1)
        if s2 < 0:
            continue
        for k in nums:
            s3 = S.find(k, s2+1)
            if s3 > 0:
                ans += 1
print(ans)