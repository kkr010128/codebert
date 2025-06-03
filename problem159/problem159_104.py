x=int(input())
k=100
a=1
for i in range(1,4000):
  k=(101*k)//100
  if k<x:
    a=a+1
print(a)
