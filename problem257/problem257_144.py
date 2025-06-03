n=int(input())
a=list(map(int,input().split()))[::-1]
number=2
if 1 not in a: print(-1);exit()
count=n-len(a[:a.index(1)+1])
a=a[:a.index(1)][::-1]
for i in a:
  if i==number:
    number+=1
  else:
    count+=1
print(count)