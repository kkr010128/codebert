N = int(input())
A = list(map(int,input().split()))
check = True

for a in A:
  if a % 2 == 0:
    if a % 3 != 0 and a % 5 != 0:
      check = False

if check:
  print("APPROVED")
else:
  print("DENIED")