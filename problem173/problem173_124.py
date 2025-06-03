import numpy as np
def main():
    n = int(input())
    x = np.arange(n + 1)
    x[x % 3 == 0] = 0
    x[x % 5 == 0] = 0
    print(x.sum())

if __name__ == '__main__':
    main()