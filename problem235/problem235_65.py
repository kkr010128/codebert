import math
n = int(input())
a = list(map(int, input().split()))
mod = int(1e+9+7)
max_val = int(1e+6+1)

def make_kago(x):
    kago = [0 for _ in range(x+1)]
    sosuu = []
    for i in range(2,x+1):
        if kago[i] != 0:
            continue
        sosuu.append(i)
        for j in range(i, x+1, i):
            if kago[j] == 0:
                kago[j] = i
    return kago, sosuu

kago, sosuu = make_kago(max_val)

def prime_factorization(x):
    if x==0 or x==1:
        return None
    soinsuu = []
    while x!=1:
        soinsuu.append(kago[int(x)])
        x = x/kago[int(x)]
    
    soinsuu_dict = dict()
    for i in range(len(soinsuu)):
        if soinsuu[i] not in soinsuu_dict:
            soinsuu_dict[soinsuu[i]] = 1
        else:
            soinsuu_dict[soinsuu[i]]+=1
    return soinsuu_dict
#%%
max_soinsuu = [0 for _ in range(int(1e+6+1))]

#%%

for i in range(n):
    soinsuu_dict = prime_factorization(a[i])
    if soinsuu_dict == None:
        continue
    for k, v in soinsuu_dict.items():
        if max_soinsuu[k] < v:
            max_soinsuu[k] = v

lcm = 1
for i in range(max_val):
    if max_soinsuu[i] != 0:
        lcm = (lcm*i**max_soinsuu[i])%mod

answer = 0
for i in range(n):
    answer = (answer + lcm*pow(a[i],mod-2,mod))%mod
    
print(answer)