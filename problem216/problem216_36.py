a, b, c = map(int, input().split())
if(a==b or a==c or c==b):
  if(a==b and b==c):
    pass
  else:
    print("Yes")
    exit()
print("No")
