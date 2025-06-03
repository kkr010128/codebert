from typing import List


def main():
    n = int(input())
    m = xyz(n)
    for i in m:
        print(i)


def f(x, y, z):
    return x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x


def xyz(n: int) -> List[int]:
    result = [0] * n
    for x in range(1, 100):
        for y in range(1, 100):
            for z in range(1, 100):
                m = f(x, y, z)
                if m > n:
                    break
                result[m - 1] += 1

    return result


if __name__ == '__main__':
    main()
