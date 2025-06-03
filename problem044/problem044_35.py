x = input().split()
a = int(x[0])
b = int(x[1])
c = int(x[2])
count = 0
# a =< b
for i in range(a,b+1):
  if c % i == 0:
    count += 1
print(count)
  
  
