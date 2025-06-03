N=int(input())
S=input()


count = 0
for i in range(1000):
  if i < 100:
    target_1 = "0"
    if i < 10:
      target_2 = "0"
      target_3 = str(i)
    else:
      target_2 = str(i)[0]
      target_3 = str(i)[1]
  else:
    target_1 = str(i)[0]
    target_2 = str(i)[1]
    target_3 = str(i)[2]
  
  step = 1
  for j in range(N):
    if S[j] == target_1 and step == 1:
      step = 2
      pass
    
    elif S[j] == target_2 and step == 2:
      step = 3
      
    elif S[j] == target_3 and step == 3:
      count += 1
      break

print(count)
      
      
    
      
    
    


    
  
