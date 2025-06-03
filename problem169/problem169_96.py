n = int(input())
a = map(int,input().split())
lst = [0]*(n+1)

for i in a:
  lst[i] += 1

for i in lst[1:]:
  print(i)