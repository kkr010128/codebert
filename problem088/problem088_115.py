n=int(input())
a=list(map(int,input().split()))

toki=a[0]
shigi=0

for i in range(1,n):
  if toki>a[i]:
    shigi += toki-a[i]
  else:toki=a[i]

print(shigi)
