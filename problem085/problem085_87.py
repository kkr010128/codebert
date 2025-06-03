import math
def GCD(a):
    gcd = a[0]
    N = len(a)
    for i in range(1, N):
        gcd = math.gcd(gcd, a[i])
    return gcd

# 素因数分解
def fact(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

n = int(input())
A = list(map(int, input().split()))
hst = [0] * (max(A) + 1)

for a in A:
    F = fact(a)
    for f in F:
        hst[f[0]] += 1
        if hst[f[0]] > 1 and f[0] != 1:
            # ここでpairwise じゃないことが確定する
            if GCD(A) == 1:
                print("setwise coprime")
            else:
                print("not coprime")
            exit()

print("pairwise coprime")