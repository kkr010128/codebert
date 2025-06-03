import fractions
n, m = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
  a[i] = a[i] //2
def count_2(k):
  c = 0
  while k % 2 == 0:
    k = k // 2
    c+=1
  return c
count = count_2(a[0])
for i in range(n):
  if count != count_2(a[i]):
    print(0)
    exit()
ans = a[0]
for i in range(1, n):
    ans = ans * a[i] // fractions.gcd(ans, a[i])
print((m // ans +1)//2)
