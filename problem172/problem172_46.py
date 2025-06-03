N=int(input())
a=int(N/100)
b=int((N-100*a)/10)
c=N-100*a-10*b
if a==7 or b==7 or c==7:
  print("Yes")
else:
  print("No")