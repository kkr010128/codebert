s=str(input())
s=list(s)
q=int(input())
sb=[0]*(q+1)
sa=[0]*(q+1)
sbi=0
sai=0
ta=0
for i in range(q):
  temp=str(input())
  temp=list(temp)
  if temp[0]=="1":
    ta=ta+1
  else:
    if (temp[2]=="1" and ta%2==0) or (temp[2]=="2" and ta%2!=0):
      sb[sbi]=temp[4]
      sbi=sbi+1
    else:
      sa[sai]=temp[4]
      sai=sai+1
lsb=sb.index(0)
lsa=sa.index(0)
sb.reverse()
ans=sb[len(sb)-lsb:len(sb)]+s+sa[0:lsa]
if ta%2!=0:
  ans.reverse()
print("".join(ans))