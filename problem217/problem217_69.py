MM = int(input())
AA = input().split()
count = 0
for j in AA:
  i = int(j)
  if i%2 ==0:
    if i%3 !=0 and i%5 !=0:
      count +=1
if count == 0:
  print('APPROVED')
else:
  print('DENIED')