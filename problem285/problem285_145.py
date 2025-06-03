def rle(t):
    tmp2, count_, ans_ = t[0], 1, []
    for i_ in range(1, len(t)):
        if tmp2 == t[i_]:
            count_ += 1
        else:
            ans_.append([tmp2, count_])
            tmp2 = t[i_]
            count_ = 1
    ans_.append([tmp2, count_])
    return ans_


S = list(input())

l = rle(S)
ans = [0] * (len(S) + 1)
count = 0
for i in range(len(l)):
    if l[i][0] == '<':
        for j in range(l[i][1] + 1):
            ans[count + j] = max(ans[count + j], j)
    elif l[i][0] == '>':
        for k in range(l[i][1] + 1):
            ans[count + k] = max(ans[count + k], l[i][1] - k)
    count += l[i][1]
print(sum(ans))
