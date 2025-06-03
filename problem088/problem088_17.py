n = int(input())
a = [int(s) for s in input().split()]

t=a[0]
total=0

for i in range(n):
  if t>a[i]:
    total=total+t-a[i]
  else:
    t=a[i]
    
print(total)