
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

ans = len(make_divisors(N-1)) - 1
#print(ans)

divisors = make_divisors(N)
def dfs(x,N):
    while N % x == 0:
        N //= x
#        print(N)
    N %= x
#    print(N)
    return N == 1

counta = 0
for i in range(1,len(divisors)):
    if dfs(divisors[i],N):
        counta += 1
#print(counta)
ans += counta

print(ans)