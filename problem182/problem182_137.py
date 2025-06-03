n, k, c = map(int, input().split())
s = input()
l = []
tmp = 0
cnt = 0
while (tmp < n):
  if s[tmp] == "o":
    l.append(tmp)
    tmp += c + 1
    cnt += 1
  else:
    tmp += 1
if cnt > k:
  exit()
l2 = []
tmp2 = n - 1
cnt2 = 0
while (tmp2 >= 0):
  if s[tmp2] == "o":
    l2.append(tmp2)
    tmp2 -= c + 1
    cnt2 += 1
  else:
    tmp2 -= 1
if cnt2 > k:
  exit()
for i in range(k):
  if l[i] == l2[k - 1 - i]:
    print(l[i]+1)