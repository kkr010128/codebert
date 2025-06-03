n,k = input().split(" ")

cost = input().split(" ")
a = []
for i in cost:
  a.append(int(i))
a.sort()

sum = 0
for i in range(int(k)):
  sum += int(a[i])
print(sum)