S=input()
result=0
count=0
for i in S:
  if i == "R":
    count+=1
    if count>result:
      result=count
  else:
    count=0
print(result)