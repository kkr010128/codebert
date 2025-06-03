s = input()
res = "" 

for i in range(len(s)):
  if s[i]!="?":
    res += s[i]
  else:
    res+="D"
print(res)