n = input()
s = list(map(int,input().split()))
m = 10000000
for p in range(0,101):
  t = 0
  for x in s:
    t+=(x-p)**2
  m = min(t,m)
print(m)