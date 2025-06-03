a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(range(1,a[0]+1))
dict = dict(zip(b,c))
for i in range(len(b)):
  print(dict.get(i+1),end=" ")