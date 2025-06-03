N,K = map(int,input().split())
count =0

for i in range(K,N+2):
  if i ==N+1:
    count+=1
  else:  
    a = (i-1)
    a = a/2
    a = a*i
    b = (N+N-(i-1))/2
    b = b*i
    count +=b-a+1
    #print(i,count,a,b)
print(int(count%(10**9+7)))