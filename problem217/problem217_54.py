n = int(input())
p = list(map(int,input().split()))

for x in p:
  if x % 2 == 0:
    if x % 3 != 0 and x % 5 != 0:
      print("DENIED")
      break

else :
  print("APPROVED")