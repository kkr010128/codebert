
t = input()
ans = ""
if t[len(t)-1] == "s":
  ans = t + "es"
else:
  ans = t + "s"
  
print(ans)