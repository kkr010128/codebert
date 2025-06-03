import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    XY = [[int(x) for x in input().split()] for _ in range(N)]

    arr1 = []
    arr2 = []
    for x, y in XY:
        arr1.append(x - y)
        arr2.append(x + y)

    print(max(abs(max(arr1) - min(arr1)), abs(max(arr2) - min(arr2))))





if __name__ == '__main__':
    main()
