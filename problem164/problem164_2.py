a,b,c,d = list(map(int,(input().split())))

ans=''
for i in range(100):
  c-=b
  if c<=0:
    ans='Yes'
    break
  a-=d
  if a<=0:
    ans='No'
    break
print(ans)