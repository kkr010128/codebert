N = int(input())

i = 1
sum = 0
while True:
  if i%3!=0 and i%5!=0:
    sum +=i
  i+=1
  if i==N+1:
    break
    
print (sum)