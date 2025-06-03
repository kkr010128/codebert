from collections import Counter
n=int(input())
a=[]
for i in range(n):
  a.append(input())
ac=Counter(a)
acs=sorted(ac.items(),key=lambda x:x[1],reverse=1)
z=len(acs)
i=0
temp=[]

while i<=z-1 and acs[i][1]==acs[0][1] :
  temp.append(acs[i][0])
  i+=1
temp.sort()
for i in temp:
  print(i)