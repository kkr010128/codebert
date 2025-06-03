S = input().split( ) 
a=int(S[0]) 
b=int(S[1])
c=int(S[2])
k=int(S[3])
t=2*a+b-k
if k <= a:
  print(str(k))
elif a < k <= a + b:
  print(str(a))
else: print(str(t))

