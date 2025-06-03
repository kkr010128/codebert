cnt = 0
zorome = 0
num = int(input())

while cnt < num:
  mass = input().split()
  
  if(mass[0] == mass[1]):
    zorome += 1
    
    if(zorome >= 3):
      break
  else:
    zorome = 0
  
  cnt += 1

print("Yes" if zorome >= 3 else "No")


