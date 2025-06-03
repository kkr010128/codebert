def max_exponent(a, n):
    # calculate k s.t. a**k <= n < a**(k+1)
    ret, v = 0, 1
    while a * v <= n:
        ret += 1
        v *= a
    return ret


def main():
    N = int(input())
    if N % 2 == 1:
        print(0)
        return
    # N is even
    count_5_in_even, pow_5 = 0, 5
    for k in range(1, max_exponent(5, N) + 1):
        count_5_in_even += (N // pow_5) // 2
        pow_5 *= 5
    count_2_in_even, pow_2 = 0, 2
    for k in range(1, max_exponent(2, N) + 1):
        count_2_in_even += N // k
        pow_2 *= 2
    print(min(count_5_in_even, count_2_in_even))


if __name__ == '__main__':
    main()