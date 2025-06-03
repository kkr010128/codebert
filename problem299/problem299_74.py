n=int(input())
a=list(map(int,input().split()))
num=["0"]*n
count="1"

for i in a:
  num[i-1]=count
  count=int(count)
  count+=1
  count=str(count)
  
print(" ".join(num))