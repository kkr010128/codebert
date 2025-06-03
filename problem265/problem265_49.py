n=int(input()) 
flag = False
for i in range(100*n,100*(n+1)):
  if i%108 == 0:
    x = int(i//108)
    print(x)
    flag = True
    break
if flag == False:
  print(':(')