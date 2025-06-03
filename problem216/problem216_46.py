a = map(int, input().split())
res = "No"
if len(set(a)) == 2:
  res = "Yes"
print(res)