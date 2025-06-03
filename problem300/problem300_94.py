def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True  

def divisors(n):
    lower_divs , upper_divs = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divs.append(i)
            if i != n // i:
                upper_divs.append(n//i)
        i += 1
    return lower_divs + upper_divs[::-1]

def resolve():
    A, B = list(map(int, input().split()))
    divs = divisors(A)
    i = 1
    cnt = 0
    while i < len(divs):
        if B%divs[i]==0 and is_prime(divs[i]):
            cnt += 1
        i += 1
    print(cnt+1)
    

if '__main__' == __name__:
    resolve()
