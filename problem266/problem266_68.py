X = int(input())

q,mod = divmod(X,100) 
#100*q<=X<=(100+5)*q
#0<=mod_x<=5q :1

if 5*q>=mod and mod>=0:
  print(1)
else:
  print(0)

