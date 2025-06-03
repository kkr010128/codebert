a = list(input())
b = list(input())
flag = True
for i,j in enumerate(a):
  if j !=b[i]:
    print('No')
    flag = False
    break
if flag == True:
  print('Yes')