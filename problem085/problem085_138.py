import math
n=int(input())
a=list(map(int,input().split()))
soin = [0]*(10**6+1)
if a.count(1)==n:
    print("pairwise coprime")
    exit()

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            while temp % i == 0:
                temp //= i
            arr.append(i)

    if temp != 1:
        arr.append(temp)

    if arr == []:
        arr.append(n)

    return arr


if len(a)>80000:
    ans=a[0]
    for i in a:
        ans=math.gcd(ans,i)
    if ans==1:
        print("setwise coprime")
    else:
        print("not coprime")
else:
    for i in a:
        if i ==1:continue
        for num in factorization(i):
            soin[num]+=1
    if max(soin)==1:
        print("pairwise coprime")
    elif max(soin)==n and 1 not in a:
        print("not coprime")
    else:print("setwise coprime")
