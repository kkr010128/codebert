N = int(input())
Llist = list(map(int,input().split()))

n =0
#print(Llist)
for i in range(N-2):
  for j in range(N-1):
    for k in range(N):
      if i<j and j<k and Llist[i]!=Llist[j] and Llist[j]!=Llist[k] and Llist[i]!=Llist[k] and Llist[i]+Llist[j]>Llist[k] and Llist[j]+Llist[k]>Llist[i] and Llist[i]+Llist[k]>Llist[j]:
        #print ('{}{}{}'.format(Llist[i], Llist[j], Llist[k]))
        #print ('{}{}{}'.format(i, j, k))
        n+=1
print(n)