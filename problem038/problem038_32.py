a,b = list(map(int, input().split()))
if a > b:
  sep = '>'
elif a < b:
  sep = '<'
else:
  sep = '=='
print('a', sep, 'b')