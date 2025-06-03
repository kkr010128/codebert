a,b,c = list(map(int,input().split()))
k = int(input())

cnt = 0

while not a < b:
  b*=2
  cnt+=1

while not b < c:
  c*=2
  cnt+=1

#print('cnt:',cnt,'k:',k)
print('Yes' if cnt <=k else 'No')