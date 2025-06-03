def fib(n):
    def iter(a, b, cnt):
        if cnt == 0:
            return a
        return iter(b, a+b, cnt-1)
    return iter(1, 1, n)

if __name__ == '__main__':
    n = int(input())
    print(fib(n))