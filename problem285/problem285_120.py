s = input()
n = len(s)
t = [0]*(n+1)
tmp=0
for i in range(n):
  tmp+=1
  if s[i]=="<":
    t[i]=tmp-1
    t[i+1]=tmp
  else:
    tmp=0
    
tmp=0
for j in range(n)[::-1]:
  tmp+=1
  if s[j]==">":
    t[j+1]=max(tmp-1,t[j+1])
    t[j]=max(tmp,t[j])
  else:
    tmp=0
#print(t)
print(sum(t))
