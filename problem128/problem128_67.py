x,n = map(int, input().split())
l = list(map(int, input().split()))
i = 0
if x not in l:
  print(x)
while x-i in l or x+i in l:
  i += 1
  if x-i not in l:
    print(x-i)
    break
  if x+i not in l:
    print(x+i)
    break