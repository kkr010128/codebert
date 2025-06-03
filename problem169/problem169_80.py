n = int(input())
an = [0 for _ in range(n)]

for i in input().split():
  an[int(i)-1] += 1

for a in an:  
  print(a)