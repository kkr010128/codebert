import numpy as np
def main():
    mod = 1000000007
    n = int(input())
    A = np.array(list(map(int, input().split())), dtype = np.int)
    ans = 0
    for i in range(61):
        n1 = np.sum((A >> i) & 1)
        tmp = (n - n1) * n1
        for _ in range(i):
            tmp = (tmp * 2) % mod
        ans += tmp
    print(ans % mod)

if __name__ == '__main__':
    main()
