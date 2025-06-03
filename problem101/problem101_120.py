A, B, C = list(map(int, input().split()))
K = int(input())
res = 0

while True:
  if B <= A:
    B *= 2
    res += 1
  else:
    break
    
while True:
  if C <= B:
    C *= 2
    res += 1
  else:
    break

if res <= K:
  print("Yes")
else:
  print("No")