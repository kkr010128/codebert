from math import ceil
debt=100000
bigets=1000
interest_rate=1.05

def calc_debt(n):
    d=debt//bigets
    while n>0:
        d=ceil(d*interest_rate)
        n -= 1
    return d*bigets
n=int(input())
print(calc_debt(n))
