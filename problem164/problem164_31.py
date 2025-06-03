A, B, C, D = map(int, input().split())

takahashi = 0
aoki = 0

while C > 0:
  C -= B
  takahashi += 1
  
while A > 0:
  A -= D
  aoki += 1
  
if takahashi <= aoki:
  print("Yes")
else:
  print("No")