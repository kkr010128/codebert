s = int(input())
if(s<3):
    print(0)
    exit()

l = s//3
cnt = 0
mod = 10**9+7
for i in range(l):
    if(i==0):
        cnt += 1
        continue

    remain = s-3*(i+1)
    bar_remain = remain+i
    n = 1
    for j in range(i):
        n*=(bar_remain-j)

    k = 1
    for j in range(1,i+1):
        k*=j

    cnt += (n//k)%mod
    cnt %= mod

print(cnt)