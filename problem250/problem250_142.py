def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    else:
        return True


def main():
    x = int(input())

    while True:
        if is_prime(x):
            ans = x
            break
        x += 1

    print(ans)


if __name__ == "__main__":
    main()
