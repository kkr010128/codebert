from math import factorial as fac

def binom(a,b):
    return(fac(a) // (fac(a-b) * fac(b)))

def main():
    S = int(input())
    count = 0
    for n in range(1,S//3 + 1):
        s = S - 3 * n
        count += binom(s+n-1,n-1)
    print(count % (10**9 + 7))
        

main()
