x = list(map(int, input().split())) 

for i in range(len(x)):
  if x[i] is 0:
    print(i+1)
