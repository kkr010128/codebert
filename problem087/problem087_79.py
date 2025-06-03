N = int(input())
n = str(N)
a = list(n)

count = 0

for i in range(len(a)):
  count = count + int(a[i])

if count % 9 == 0:
  print("Yes")
else:
  print("No")