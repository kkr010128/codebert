n=int(input())
A=list(map(int,input().split()))
for i in A:
  if i%2==1 or i%3==0 or i%5==0:
    continue
  print("DENIED")
  exit()
print("APPROVED")