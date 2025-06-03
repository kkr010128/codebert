n=int(input())
a=list(map(int, input().split()))

joushi = [0]*(n+1)
for i in range(n-1):
  joushi[a[i]] += 1
del joushi[0]

for i in range(len(joushi)):
  print(joushi[i])
