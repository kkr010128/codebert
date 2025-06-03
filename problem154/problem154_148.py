N,K = map(int,input().split())

sunuke = [0]*(N+1)
for i in range(K):
  okashi_category = input()
  #print (okashi_category)
  if okashi_category ==1:
    sunuke[input()]=1
  else:
    sunukelist = list(map(int,input().split()))
    for j in range(len(sunukelist)):
      #print(sunukelist[j])
      sunuke[sunukelist[j]]=1

print (N-sum(sunuke))