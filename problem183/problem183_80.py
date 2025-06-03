n = int(input());div=[];ans=[]
for i in range(1,int(n**0.5)+2):
  if n%i == 0:
    div.append(i);div.append(n//i)
    
for i in div:
  if i == 1:
    continue
  tmp = n
  while tmp % i == 0:
    tmp //= i
  if tmp % i ==1:
    ans.append(i)
    
n -= 1
for i in range(1,int(n**0.5)+2):
  if n%i == 0:
    ans.append(i);ans.append(n//i)
    
print(len(set(ans))-1)