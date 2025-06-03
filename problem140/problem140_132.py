n=input()
m=len(n)
li=[]
for i in range(m):
  li.append(n[i])

for i in range(len(li)):
  if li[i]=="?":
    li[i]="D"
  else:
    pass

print("".join(li))