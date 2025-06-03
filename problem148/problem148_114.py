A,B,C,K = map(int,input().split())

koa = 0
if A<K:
  koa = A
else :
  koa = K
kob = 0
if B<K-koa:
  kob = B
else :
  kob = K-koa
#print (koa)
#print (kob)
sum = koa+0*kob+(K-(koa+kob))*-1
print (sum)