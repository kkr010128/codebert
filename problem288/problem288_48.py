n = int(input())
 
b = 10**12
a = int((n**0.5)//1)
for i in range(1,a+1):
  if n%i==0:
    b = min(b,int(i+(n//i)-2))
print(b)