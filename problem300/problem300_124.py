def factorization(n):
    arr = set()
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.add(i)

    if temp!=1:
        arr.add(temp)

    if arr==[]:
        arr.add(n)

    return arr

a,b = map(int, input().split())
a_soi = factorization(a)
b_soi = factorization(b)
both = list(a_soi & b_soi)
print(len(both)+1)