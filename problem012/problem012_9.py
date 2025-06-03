import sys


def sieve(N):
    is_prime = [True] * (N + 1)
    prime_list = []
    
    is_prime[0] = is_prime[1] = False
    
    prime_list.append(2)
    for i in range(3, N + 1, 2):
        if is_prime[i]:
            prime_list.append(i)
        for j in range(i * i, N, i):
            is_prime[j] = False
    
    return prime_list
    
primes = sieve(10001)
primes_set = set(primes)

def is_prime(num):
    if num in primes_set:
        return True
    elif num <= 10000:
        return False
    else:
        for prime in primes:
            if num % prime == 0:
                return False
        return True
    
if __name__ == '__main__':
    N = sys.stdin.readline()
    N = int(N)
    ans = 0
    for i in range(N):
        num = sys.stdin.readline()
        num = int(num)
        if is_prime(num): ans += 1
    
    sys.stdout.write(str(ans) + '\n')