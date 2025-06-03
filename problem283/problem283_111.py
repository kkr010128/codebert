
import math

if __name__ == "__main__":
    N = int(input())
    if N % 2 == 0:
        hoge = N / 2
        print(math.floor(hoge) - 1)
    else:
        print(math.floor(N / 2))
