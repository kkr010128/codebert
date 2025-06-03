# 素因数分解

N=int(input())
cand=[]

def check(N0,K0):
    if N0%K0==0:
        return check(int(N0/K0),K0)
    elif N0%K0==1:
        return 1
    else:
        return 0

def check0(N0,K0):
    while N0%K0==0:
        N0=int(N0/K0)
    if N0%K0==1:
        return 1
    else:
        return 0

# N-1の約数の数
for i in range(2,int((N-1)**0.5)+1):#O(N**0.5)
    if (N-1)%i==0:
        cand.append(i)
        if i!=int((N-1)/i):
            cand.append(int((N-1)/i))
if N>2:
    cand.append(N-1)

# Nの約数
for i in range(2,int(N**0.5)+1):#O(N**0.5)
    if N%i==0:
        cand.append(i)
        if i!=int(N/i):
            cand.append(int(N/i))
cand.append(N)

#print(cand)
count=0
for i in range(len(cand)):
    if check(N,cand[i]):
        count+=1

print(count)