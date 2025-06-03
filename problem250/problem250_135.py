def find_prime(x):
    while True:
        if x == 2:
            return x
        else:
            for i in range(2, x+1):
                if x % i == 0:
                    if i == x:
                        return x
                    else:
                        break
                else:
                    continue
            x += 1


def main():
    x = int(input())

    x = find_prime(x)

    print(x)


if __name__ == "__main__":
    main()
