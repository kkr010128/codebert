N = int(input())
a = list(map(int,(input().split())))
list_a = [0]*2*100001
for i in a:
  list_a[i] += 1
for i in range(1,N+1):
  print(list_a[i])