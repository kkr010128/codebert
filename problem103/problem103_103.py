# import math
# import statistics
a=int(input())
#b,c=int(input()),int(input())
# c=[]
# for i in a:
#    c.append(i)
#e1,e2,e3 = map(int,input().split())
#K = input()
f = list(map(int,input().split()))
#g = [input() for _ in range(a)]
now=1000
buy=0
sell=0
kabu=0
for i in range(a-1):
    if f[i]<f[i+1]:
        if now>=f[i]:
            buy=now//f[i]
            now=now-buy*f[i]
            kabu=buy
            buy=0
    if f[i]>f[i+1] :
        if kabu>=1:
            sell=kabu
            now=now+sell*f[i]
            kabu=0
            sell=0
    if f[i]==f[i+1]:
        continue
now = now+f[-1]*kabu
print(now)
        
        

