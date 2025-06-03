from collections import defaultdict
n = int(input())
dct = defaultdict(int)
for i in range(1,n+1):
    s = str(i)
    dct[(s[0],s[-1])] += 1
ans = 0
for i in range(1,n+1):
    s = str(i)
    ans += dct[(s[-1],s[0])]
print(ans)