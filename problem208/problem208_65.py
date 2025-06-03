n, m = map(int, input().split())
nums = [0] * n
check_flgs = [0] * n
cnt = 0
for _ in range(m):
    s, c = map(int, input().split())
    if check_flgs[s-1] == 0:
        nums[s-1] = c
        cnt += 1
        check_flgs[s-1] = 1
    elif check_flgs[s-1] != 0:
        if nums[s-1] == c:
            cnt += 1
            continue
        else:
            break
ans = ""
for num in nums:
    ans += str(num)
if cnt == m and n == 1:
    print(int(ans))
elif cnt == m and n >= 2 and nums[0] != 0:
    print(int(ans))
elif cnt == m and n >= 2 and nums[0] == 0 and check_flgs[0] == 0:
    print("1" + ans[1:])
else:
    print("-1")