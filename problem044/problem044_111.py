a,b,c = map(int,input().split()) ;
count = 0 ;
for i in range(a,b+1) :
  d = c % i ;
  if d == 0 :
     count = count +1

print("%d" % count) 