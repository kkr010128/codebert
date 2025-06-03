k = int(input())
a, b = map(int, input().split())

f = False
for x in range(a, b+1):
  if x % k == 0:
    f = True
    
print('OK' if f else 'NG')