N=int(input())
A=list(map(int,input().split()))
count=0
mi=N+1
for a in A:
  if a < mi:
    count+=1
    mi = a
print(count)