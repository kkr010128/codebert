N,M = map(int,input().split())

Alist = list(map(int,input().split()))

Alist = sorted(Alist,reverse=True)
#print (sum(Alist))
Ans = "No"
for i in range(M):
  #print (Alist[i])
  #print((sum(Alist)/4*M))
  if Alist[i]>=(sum(Alist)/(4*M)):
    Ans ="Yes"
  else:
    Ans = "No"
    
print (Ans)