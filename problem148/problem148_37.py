a,b,c,k=map(int,input().split())
ai=0
bi=0
ci=0
if a >= k:
  ai=k
else:
  ai=a
  if b>= k-ai:
    bi=k-ai
  else:
    bi=b
    ci= k - ai - bi
print(ai-ci)
        
