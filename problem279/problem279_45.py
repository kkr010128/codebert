if(int(input()) %2 == 1):
  print("No")
  exit()
t = input()
if(t[:len(t)//2] == t[len(t)//2:]):
  print("Yes")
else:
  print("No")
