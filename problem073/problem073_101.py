#!/usr/bin/env python

class PrimeFactor():
    def __init__(self, n):
        '''
            Note:
                make the table of Eratosthenes' sieve
                and minFactor[] for fast_factorization.
        '''
        self.n = n
        self.table = [True for _ in range(n+1)]
        self.table[0] = self.table[1] = False
        self.minFactor = [-1 for _ in range(n+1)]

        for i in range(2, n+1):
            if not self.table[i]: continue
            self.minFactor[i] = i 
            for j in range(i*i, n+1, i): 
                self.table[j] = False
                self.minFactor[j] = i 
    
    def fast_factorization(self, n):
        '''
            Note:
                factorization
                return the form of {factor: num}.
        '''
        data = {}
        while n > 1:
            if self.minFactor[n] not in data:
                data[self.minFactor[n]] = 1 
            else:
                data[self.minFactor[n]] += 1
            n //= self.minFactor[n]
        return data

    def count_divisors(self, n):
        '''
            Note:
                return the number of divisors of n.
        '''
        ret = 1 
        for v in self.fast_factorization(n).values():
            ret *= (v+1)
        return ret 

n = int(input())
ans = 0
a = PrimeFactor(n)
for i in range(1, n): 
    ans += a.count_divisors(i)
print(ans)
