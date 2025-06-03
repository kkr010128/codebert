n = int(input())
a_ls = list(map(int, input().split()))

next_number = 1
ans = 0
for i in range(n):
    if a_ls[i] == next_number:
        next_number += 1
    else:
        ans += 1
if ans == n:
    ans = -1
print(ans)
