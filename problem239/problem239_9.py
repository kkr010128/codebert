x = 'abcdefghijklmnopqrstuvwxyz'
c = str(input())
for i,data in enumerate(x):
  if data == c:
    print(x[i+1])
    break