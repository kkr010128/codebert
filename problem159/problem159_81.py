X=int(input())
i=0
t=100
while(t<X):
  t *= 101
  t = int(t//100)
  i += 1
print(i)