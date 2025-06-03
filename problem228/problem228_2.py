H = int(input())

i=0
count=0
while(H>0):
  H=H//2
  count += 2**i
  i+=1
  
print(count)