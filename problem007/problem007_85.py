def main():
    N = int(input())
    if N <= 1:
        print(1)
        return
    fib = [0]*(N+1)
    fib[0], fib[1] = 1, 1
    for i in range(2, N+1):
        fib[i] = fib[i-1] + fib[i-2]
    print(fib[N])


if __name__ == "__main__":
    main()
