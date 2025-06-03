N = int(input())
a = []
for i in range(10):
  for j in range(10):
    a.append(i * j)
 
print("Yes") if N in a else print("No")