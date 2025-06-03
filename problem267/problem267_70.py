import collections
n = int(input())
s = input()
ans = 0
for i in range(10):
    ind = s.find(str(i))+1
    if ind == 0 or ind == len(s):
        continue
    for j in range(10):

        ind_j = ind + s[ind:].find(str(j))+1
        if ind_j == ind or ind_j == len(s):
            continue
        cnt = collections.Counter(s[ind_j:])
        ans += len(cnt)

print(ans)
