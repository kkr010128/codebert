a=int(input())
b=100
i=0
while b<a:
  b+= b // 100
  i+=1
print(i)