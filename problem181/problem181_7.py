k = int(input())
cand = [[1,2,3,4,5,6,7,8,9]]
for i in range(9):
  tmp = []
  for val in cand[-1]:
    if val % 10 != 0:
      tmp.append(val*10 + (val%10 - 1))
    tmp.append(val*10 + (val % 10))
    if val % 10 != 9:
      tmp.append(val*10 + (val%10 + 1))
  cand.append(tmp)

ans = []
for j in range(len(cand)):
  for val in cand[j]:
    ans.append(val)
ans = sorted(ans)

print(ans[k - 1])
