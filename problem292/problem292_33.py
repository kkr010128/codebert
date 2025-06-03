N = int(input())
Tot = 0
d = [int(x) for x in input().split()]  
for i in range(N):
  for j in range(N):
    if i > j:
      # print(i , j)
      Tot += d[i] *d[j]
print(Tot)