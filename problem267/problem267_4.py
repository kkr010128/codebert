n=int(input())
s=input()
ans=0
for i in range(1000):
  i='0'*(3-len(str(i)))+str(i)
  if i[0] in s:
    if i[1] in s[s.index(i[0])+1:]:
      if i[2]in s[s.index(i[0])+s[s.index(i[0])+1:].index(i[1])+2:]:
        ans+=1
print(ans)