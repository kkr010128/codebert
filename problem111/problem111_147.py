# 降順にしたものを考え、最大のやつは1回、あとのやつは2回ずつ使える
n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
ans = a[0]
count = n - 2
idx = 1
while count > 0:
    count_of_count = 2
    while count_of_count > 0 and count > 0:
        count -= 1
        count_of_count -= 1
        ans += a[idx]
    idx += 1
print(ans)