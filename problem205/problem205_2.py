n, p = map(int, input().split())
s = input()

count = [0]*p

key = 0
if p%2 and p%5:
  count = [0]*p
  key = 0
  
  mod = 1
  for i in range(n):
    key += (mod*int(s[n-1-i]))%p
    key %= p
    count[key] += 1
    mod *= 10
    mod %= p
  ans = count[0]
  for i in range(p):
    if count[i] >= 2:
      ans += (count[i])*(count[i]-1)//2
else:
  ans = 0
  for i in range(n):
    key = int(s[n-1-i])
    if key%p == 0:
      ans += n-i
print(ans)