from math import ceil


def main():
    n = int(input())

    min_value = n * 100 / 108
    max_value = (n + 1) * 100 / 108

    candidate = ceil(min_value)

    if candidate < max_value:
        print(candidate)
    else:
        print(":(")


if __name__ == "__main__":
    main()
