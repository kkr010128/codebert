n = int(input())

tmp = int(n/1.08)
ans_lists = [tmp + i for i in range(2)]
ans = 0
for j in ans_lists:
    if int(j*1.08) == n:
        ans = j
        break
    else:
        ans = ':('

print(ans)