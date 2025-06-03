A,B,C = map(int, input().split())
K = int(input())

for i in range(K):
  if B >= C or  A >= C:
    C *= 2
  else:
    if A >= B:
      B *= 2
if C > B and B > A:
  print("Yes")
else:
  print("No")