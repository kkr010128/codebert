from collections import Counter
n = int(input())
s = Counter([input() for _ in range(n)])
before = 0
ans = []
s = s.most_common()
for i in range(len(s)):
    if before == 0: before = s[i][1]
    elif before != s[i][1]: break
    ans.append(s[i][0])
for i in sorted(ans): print(i)