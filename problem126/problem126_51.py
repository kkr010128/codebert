x_list = list(map(int, input().split()))
ans = 0
for i, x in enumerate(x_list):
    if x == 0:
        ans = i + 1
        break
print(ans)
