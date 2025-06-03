# Papers, Please

N = int(input())
A = list(map(int, input().split()))

for Ai in A:
  if Ai % 2 == 1:
    continue
  else:
    if Ai % 3 != 0 and Ai % 5 != 0:
      print("DENIED")
      exit()

print("APPROVED")