k = int(input())
rep = 0
f = 0
for i in range(k):
    rep=  rep*10 + 7
    if(rep%k == 0):
        f = 1
        break
    rep = rep%k
print(-1 if(f == 0) else i+1)