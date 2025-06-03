N = int(input())
a = list(map(int, input().split()))
count = 1
bk = 0
for i in a:
    if i == count:
        count += 1
    else:
        bk += 1
if bk == N:
    ans = -1
else:
    ans = bk
print(ans)
