N = input()
s1 = []
s2 = []
res = []
ans = []
cnt = 0
for i in range(len(N)):
    if N[i] == "\\":
        s1.append(i)
    elif N[i] == "/" and s1:
        idx = s1.pop()
        tmp = i - idx
        cnt += tmp

        while s2 and idx < s2[-1][0]:
            tmp += s2.pop()[1]
        s2.append((idx, tmp))

res.append(len(s2))
for i in range(len(s2)):
    ans.append(s2[i][1])
res.extend(ans)
print(cnt)
print(" ".join(map(str, res)))
