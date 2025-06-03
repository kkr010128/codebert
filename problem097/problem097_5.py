K = int(input())

cnt=1
Num=7%K
while cnt<=K:
  if K%2==0:
    print('-1')
    break
  if Num%K==0:
    print(cnt)
    break
  else:
    Num = (10*Num + 7)%K
    cnt+=1
else:
  print('-1')

