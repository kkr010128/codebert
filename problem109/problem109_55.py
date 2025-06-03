n=int(input())

ans=[]

for i in range(n):
  ans.append(input())
  
def func(ans,moji):
  num=ans.count(moji)
  print(moji,"x",str(num))

mojis=["AC","WA","TLE","RE"]
for moji in mojis:
	func(ans,moji)