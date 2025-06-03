X,N = map(int,input().split())

min = 100

if N !=0:
  Plist = list(map(int,input().split()))
  anslist = [i for i in range(102)]
  anslist.append(-1)
  #anslist.remove(0)
  Plist = sorted(Plist)
  #print (anslist)
  for i in range(N):
    anslist.remove(Plist[i])
    temp =100
  for i in range(len(anslist)):
    if min >abs(anslist[i]-X) :
      min = abs(anslist[i]-X)
      temp = anslist[i]
  print (temp)
else :
  print (X)