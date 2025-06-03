n=int(input())
while 1:
  for i in range(2,int(n**0.5)+1):
    if n%i<1: break
  else: print(n); break
  n+=1