

A, B = map(int, input().split())

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

    return arr

a_fac = factorization(A)
b_fac = factorization(B)
ans = 0
is_one = False
for af in a_fac:
    for bf in b_fac:
        if af[0] == bf[0]:
            ans += 1
            if af[0] == 1:
                is_one = True
if is_one:
    print(ans)
else:
    print(ans+1)