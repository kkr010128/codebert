n = int(input())
a = list(map(int, input().split()))

x = n//2
if sum(a)/2 == sum(a[:(n//2)]):
  print(0)
elif sum(a)/2 >= sum(a[:(n//2)]):
  while sum(a)/2 >= sum(a[:x]):
    x += 1  
  print(min(abs(2*sum(a[:x])-sum(a)), abs(2*sum(a[:x-1])-sum(a))))
else:
  while sum(a)/2 <= sum(a[:x]):
    x -= 1
  print(min(abs(2*sum(a[:x])-sum(a)), abs(2*sum(a[:x+1])-sum(a))))
