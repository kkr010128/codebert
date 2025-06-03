a,b = map(int,input().split())
x = ''
if a < b:
  x = ' < '
elif a > b:
  x = ' > '
else:
  x = ' == '
print('a'+x+'b')