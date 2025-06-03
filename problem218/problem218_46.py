from collections import Counter
N = int(input())
S = [input() for _ in range(N)]
cntr = Counter(S)
mc = cntr.most_common()
n = mc[0][1]
ans = []
for k, v in mc:
    if n!=v:
        break
    ans.append(k)
ans.sort()
print("\n".join(ans))
