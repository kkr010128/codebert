N=int(input())
A=list(map(int,input().split()))
Q=int(input())

NumList=[0]*(10**5+1)

AllSum=sum(A)

for a in A:
  NumList[a]+=1

for i in range(Q):
  B,C=map(int,input().split())
  AllSum=AllSum + (C-B)*NumList[B]
  NumList[C]+=NumList[B]
  NumList[B]=0
  
  print(AllSum)