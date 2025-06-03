import math


def main():
    hp, attack = (int(i) for i in input().rstrip().split(' '))
    print(str(math.ceil(hp / attack)))


if __name__ == '__main__':
    main()

