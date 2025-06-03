import math

def main():
    A, B = map(int, input().split())
    a_min = int(math.ceil(A / 0.08))
    a_max = int(math.floor((A+1) / 0.08)) - 1
    b_min = 10 * B
    b_max = 10 * (B+1) - 1
    if a_max < b_min or b_max < a_min:
        print(-1)
    else:
        print(max([a_min, b_min]))


if __name__ == '__main__':
    main()
