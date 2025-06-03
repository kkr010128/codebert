li=list(map(int,input().split()))
for i in li:
  if li.count(i)==2:
    print("Yes")
    break
else:
  print("No")