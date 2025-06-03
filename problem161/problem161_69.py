import math

def main():
    A, B, N = map(int, input().split())
    x = min([B-1, N])
    print(int(math.floor(A * x / B) - A * math.floor(x / B)))


if __name__ == '__main__':
    main()
