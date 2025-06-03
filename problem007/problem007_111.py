def main():
    n = input()
    F = [0]*(n+1)
    number = fibonacci(n,F)
    print number

def fibonacci(n,F):
    if n == 0 or n == 1:
        F[n] = 1
        return 1
    if F[n] != 0:
        return F[n]
    else:
        F[n] = fibonacci(n-2,F)+fibonacci(n-1,F)
        return F[n]

if __name__ == "__main__":
    main()