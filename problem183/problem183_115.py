N = int(input())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    # divisors.sort()
    return divisors

K = []
# N = K**n*(K*m+1)
# n >= 1

K1 = make_divisors(N)
K1.pop(0)
# print(K1)

for k in K1:
    # print("k=",k)
    n=0
    while N-k**n >= 0:
        # print((N-k**n)%(k**(n+1)))
        # print("n=",n)
        if (N-k**n)%(k**(n+1))==0:
            K.append(k)
        n += 1
# print(K)

# n == 0
K2 = make_divisors(N-1)
K2.pop(0)
K += K2

# print(K)

print(len(K))

