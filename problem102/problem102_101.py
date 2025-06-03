n, k = map(int, input().split())
a = [int(x) for x in input().split()]

for i in range(n-k):
  if a[i+k] > a[i]:
    print("Yes")
  else:
    print("No")