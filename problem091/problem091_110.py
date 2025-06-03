n=int(input())
l=[int(i) for i in input().split()]
 
l.sort()
 
def func(one,two,three):
  if len({one,two,three})==3 and one+two>three:
    return True
  return False
 
ans=0
for i in range(n-2):
  for j in range(i+1,n-1):
    for k in range(j+1,n):
      one=l[i]
      two=l[j]
      three=l[k]
      if func(one,two,three):
        ans+=1
        
print(ans)