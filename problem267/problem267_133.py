n=int(input())
s=input()
c=0
for i in range(1000):
  t=format(i,"0>3")
  j=0
  for k in s:
    if k==t[j]:
      j+=1
      if j==3:
        c+=1
        break
print(c)