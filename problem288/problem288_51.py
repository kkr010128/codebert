N = int(input())
p = 1

for i in range(1,int(N**0.5+1)):
  if N%i == 0:
    p = i
    
print(p+N//p-2)