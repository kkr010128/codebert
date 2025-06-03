n = int(input())
x = list(map(int,input().split()))
for i in x:
  if i%2==0:
    if i%6!=0:
      if i%10!=0:
        print("DENIED")
        exit()
print("APPROVED")