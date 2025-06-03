mojiretsua=input()
mojiretsub=input()
count=0
for i in range(len(mojiretsua)):
  if mojiretsua[i] != mojiretsub[i]:
    count=count+1
print(count)