s=str(input())
s=list(s)
if s[len(s)-1]=="s":
  print("".join(s)+"es")
else:
  print("".join(s)+"s")