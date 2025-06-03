import sys
N=int(input())

if N==2:
  print(1)
  sys.exit(0)

answer_set=set()
for i in range(2,int(N**0.5)+1):
  N2=N
  while N2%i==0:
    N2//=i
  if N2%i==1:
    answer_set.add(i)
#print(answer_set)

for i in range(1,int(N**0.5)+1):
  if (N-1)%i==0:
    answer_set.add((N-1)//i)    
#print(answer_set)

answer_set.add(N)
print(len(answer_set))