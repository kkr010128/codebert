N,M = map(int,input().split())
 
if N>=2:
  gyu = N*(N-1)//2
else:
  gyu = 0
  
if M>=2:
  ki = M*(M-1)//2
else:
  ki = 0
 
print(gyu+ki)