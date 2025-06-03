HP, n = map(int,input().split())
a = list(map(int,input().split()))
count = 0

for i in a:
  count += i
if count >= HP:
  print("Yes")
else:
  print("No")