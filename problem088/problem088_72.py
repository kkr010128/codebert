n = int(input())
a = list(map(int,input().split()))
b = a[0]
x = 0
for i in range(1,n):
  if a[i] > b:
    b = a[i]
  else:
    x += b-a[i]
print(x)