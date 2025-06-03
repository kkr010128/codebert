N = int(input())
s = list(map(int , input().split()))
list.sort(s , reverse = True)
L = [10**10]
for p in range(min(s) , max(s) + 1):
  a = 0
  b = L[0]
  for i in range(N):
    if a < b:
      a += (s[i] - p) ** 2
  if a < b:
    L[0] = a
print(L[0])