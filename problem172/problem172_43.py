n = int(input())
k = n//10
if n%10 == 7:
  print("Yes")

elif k%10 == 7:
  print("Yes")

elif n//100 == 7:
  print("Yes")

else:
  print("No")