a,b=map(str,input().split())
res = ""
if a < b:
  for i in range(int(b)):
    res += a
else:
  for i in range(int(a)):
    res += b
print(res)