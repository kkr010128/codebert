A, B, C = map(int, input().split())
K = int(input())

num = 0
while B <= A:
  B *= 2
  num += 1
while C <= B:
  C *= 2
  num += 1
  
if num > K:
  print("No")
else:
  print("Yes")