import itertools
import collections

class PrimeFactorize:
    def __init__(self, n):
        self.prime_factor_table = self.create_prime_factor_table(n)

    # O(NloglogN)
    def create_prime_factor_table(self, n):
        self.table = [0] * (n + 1)
        
        for i in range(2, n + 1):
            if self.table[i] == 0:
                for j in range(i + i, n + 1, i):
                    self.table[j] = i
        return self.table

    def prime_factor(self, n):
        prime_count = collections.Counter()
        
        while self.prime_factor_table[n] != 0:
            prime_count[self.prime_factor_table[n]] += 1
            n //= self.prime_factor_table[n]
        prime_count[n] += 1
        return prime_count

N = int(input())
pf = PrimeFactorize(10**5+5)

for i in range(N,10**5+5):
    if pf.prime_factor_table[i]==0:
        print(i)
        break