n = int(input())
S = 0
for i in range(1,n+1):
  a = n//i
  j = i * a
  s = (i+j)*a//2
  S += s
  
print(S)  
  
