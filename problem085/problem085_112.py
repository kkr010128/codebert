n = int(input())
a = list(map(int, input().split()))

M = max(a)
biggest_prime = [0] * (M+10)
for i in range(2, M+10):
    if biggest_prime[i] == 0:
        biggest_prime[i] = i
        for j in range(i*i, M+1, i):
            biggest_prime[j] = i

def fact(n):
    arr=[]
    while n>1:
        now=n
        cnt=0
        p=biggest_prime[now]
        while now % p == 0:
            now//=p
            cnt+=1
        arr.append([p,cnt])
        n=now
    return arr

from collections import defaultdict
cntd=defaultdict(int)
for i in range(len(a)):
    lis = fact(a[i])
    for num,cnt in lis:
        if num==1:
            continue
        cntd[num]+=1
flg=False
for c in cntd.values():
    if c==n:
        print("not coprime")
        exit()
    if c>1:
        flg=True
if flg:
    print("setwise coprime")
else:
    print("pairwise coprime")