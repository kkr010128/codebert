s = input()

# now = 0
left = 0
right = 0
ans = []
for i in range(len(s) + 1):
    if left == 0:
        # 左側
        for j in range(i - 1, -1, -1):
            if s[j] != '<':
                break
            else:
                left += 1
    else:
        if s[i - 1] == '<':
            left += 1
        else:
            left = 0
    # 右側
    if right == 0:
        for j in range(i, len(s)):
            if s[j] != '>':
                break
            else:
                right += 1
    else:
        if i == len(s):
            right = 0
        elif s[i] == '>':
            right -= 1
        else:
            right = 0
    ans.append(max(left, right))
# print(ans)
print(sum(ans))
