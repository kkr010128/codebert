n=int(input())
s=input()
cnt=0
for m in range(1000):
  m=str(m).zfill(3)
  j=0
  for i in m:
    if i not in s[j:]:break
    j+=s[j:].index(i)+1
  else:cnt+=1
print(cnt)