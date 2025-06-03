import sys,fractions
input = sys.stdin.readline

a,b = map(int,input().split())
g = fractions.gcd(a,b)

if g == 1:
    print(1)
    exit()

def factorization(n):
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

    return len(arr)+1


print(factorization(g))
