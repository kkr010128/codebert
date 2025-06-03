def main():
    N = int(input())
    I = tuple(int(input()) for _ in range(N))

    ans = 0
    for i in I:
        if is_prime(i):
            ans += 1
    print(ans)

def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if i * i > n:
                break
            elif n % i == 0:
                return False
        return True

main()