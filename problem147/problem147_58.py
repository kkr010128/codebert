a= input()
b = input()
if b[0:-1] == a:
  if len(a) + 1 == len(b):
    print('Yes')
    exit()
print('No')