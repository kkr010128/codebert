T = list(map(str, input()))
count = 0
ans = []




for i in range(0, len(T)):
    if T[i] == '?':
        ans.append('D')
    else:
        ans.append(T[i])


ans_ans = ''.join(ans);

print(ans_ans)
