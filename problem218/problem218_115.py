n=int(input())

dic={}
for i in range(n):
  s=input()
  if s not in dic:
    dic[s]=1
  else:
    dic[s]+=1


dic = sorted(dic.items(),key=lambda x:x[0])
dic = sorted(dic,key=lambda x:x[1],reverse=True)

ma=dic[0][1]
for i,v in dic:
  if v!=ma:
    break
  else:
    print(i)