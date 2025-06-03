N,M=map(int,input().split())
a=N//2
b=a+1
print(a,b)
if M==1:
  exit(0)
c=1
d=N-1
print(c,d)
for i in range(M-2):
  if i%2==0:
    a,b=a-1,b+1
    print(a,b)
  else:
    c,d=c+1,d-1
    print(c,d)
