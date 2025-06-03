import math
n=int(input())
a=list(map(int,input().split()))
mxa=max(a)

def get_sieve_of_eratosthenes(mxa):
    fact = [0]*(mxa+1)
    limit = int(math.sqrt(mxa))
    for i in range(2,limit+1):
        if fact[i]!=0:
            continue
        else:
            fact[i]=i
            for j in range(i, mxa+1, i):
                if fact[j]==0:
                    fact[j]=i
    for i in range(2,mxa+1):
        if fact[i]==0:
            fact[i]=i

    return fact

fact = get_sieve_of_eratosthenes(mxa)

lst=[0]*(len(fact))
for i in range(n):
    divisor = set()
    while a[i]!=1:
        divisor.add(fact[a[i]])
        a[i]//=fact[a[i]]
    for d in divisor:
        lst[d]+=1

pair=True
st=True

for i in lst:
    if i>=2:
        pair=False
    if i==n:
        st=False
if pair:
    print("pairwise coprime")
elif st:
    print("setwise coprime")
else:
    print("not coprime")
