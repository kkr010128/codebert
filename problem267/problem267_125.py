n = int(input())
s = list(input())
ans = 0

for i in range(0, 1000):
    count = 0
    val = list(str(i).zfill(3))
    k = val[count]
    for j in s:
        if j == k:
            count += 1
            if count <= 2:
                k = val[count]
            elif count == 3:
                ans += 1
                break
print(ans)

