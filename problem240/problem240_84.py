N,M = map(int,input().split())
wa_list= [0]*(N+2)
ac_list=[-1]*(N+2)
for i in range(M):
  p,a = map(str,input().split())
  p = int(p)
  if a =='WA':
    wa_list[p]+=1
  if a =='AC' and ac_list[p] == -1:
    ac_list[p]+=(wa_list[p]+1)
count = 0;count2 = 0
for i in ac_list:
  if i>=0:
    count+=1
    count2+=i
print(count,count2)
    
