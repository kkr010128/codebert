n = int(input())
lst = list(map(int,input().split()))
c = 0
for i in range(n):
  if (lst[i]%2 == 0):
    if (lst[i]%3 != 0 and lst[i]%5 != 0):
      c = 1
if (c == 0):
  print("APPROVED")
else:
  print("DENIED")
