numbers = []
while True:
  x=int(input())
  if x==0:
    break
  numbers.append(x)

for i in range(len(numbers)):
  print("Case ",i+1,": ",numbers[i],sep="")

