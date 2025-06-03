from fractions import gcd  # for python 3.5~, use math.gcd


def main():
    N, M = list(map(int, input().split(' ')))
    half_A = list(map(lambda x: int(x) // 2, input().split(' ')))
    lcm = 1
    for half_a in half_A:
        lcm *= half_a // gcd(lcm, half_a)
        if lcm > M:
            print(0)
            exit(0)
    for half_a in half_A:
        if (lcm // half_a) % 2 == 0:
            print(0)
            exit(0)
    num_multiples = M // lcm
    print((num_multiples + 1) // 2)  # count only cases that ratios are odd numbers.


if __name__ == '__main__':
    main()