x=int(input())

i=0
while (i+1)*100 <= x:
  i+=1
  nokori = x-i*100
  num = ((nokori - 1) // 5) + 1 
  
  if num <= i:
    print(1)
    exit()
    
print(0)