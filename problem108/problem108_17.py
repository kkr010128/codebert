N = int(input())

i = 1
while True:
  M = 1000*i
  if M >= N:
    break
  
  i += 1
    
ans = M-N

print(ans)