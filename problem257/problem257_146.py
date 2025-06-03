n = input()
list = map(int, input().split())
 
num = 1
a = 0
 
for i in list:
  if i == num:
    num = num +1
  else:
    a = a + 1
 
if num == 1:
  print(-1)
else:
  print(a)