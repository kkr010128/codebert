import collections

n = int(input())
a = list(map(int, input().split()))

b = [0] * n
c = [0] * n
for i in range(n):
  b[i] = a[i] + (i + 1)
  c[i] = (i + 1) - a[i]

ans = 0
cCc = collections.Counter(c)
# print(cCc)
for k, v in collections.Counter(b).items():
  if v != 0 and k in cCc:
    # print(k,v,cCc[k])
    ans += v * cCc[k]

print(ans)
