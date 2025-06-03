N = int(input())
l = list(map(int, input().split()))

counter = 1
ans = 0

for j in l:
    if j == counter:
        counter += 1
    else:
        ans += 1

if counter==1:
    print(-1)
else:
    print(ans)