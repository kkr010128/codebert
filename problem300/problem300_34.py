a,b = map(int,input().split())

if min(a,b) == 1:
    print(1)
    exit()

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            while temp%i==0:
                temp //= i
            arr.append(i)
    if temp!=1:
        arr.append(temp)
    if arr==[]:
        arr.append(n)
    return arr

A = factorization(a)
B = factorization(b)
ans = len(set(A) & set(B))
print(ans+1)

