n = int(input())
a = list(map(int, input().split()))
okane = 1000
kabu = 0
for i in range(n-1):
  if a[i] > a[i+1]:
    okane += kabu * a[i]
    kabu = 0
  elif a[i] < a[i+1]:
    kabu += okane // a[i]
    okane = okane % a[i]
r = okane + kabu * a[n-1]
print(r)