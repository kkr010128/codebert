import sys
from math import gcd
def input(): return sys.stdin.readline().strip()

def main():
    N = int(input())
    A =list(map(int, input().split()))

    all_gcd = A[0]
    max_num = A[0]
    for a in A:
        all_gcd = gcd(all_gcd, a)
        max_num = max(max_num, a)
    if all_gcd != 1:
        print("not coprime")
        return

    # エラトステネスの篩でmin_prime[i] = (iを割り切る最小の素数)を記録する
    min_prime = [i for i in range(max_num + 1)]
    for p in range(2, int(max_num**0.5) + 1):
        if min_prime[p] != p: continue
        for i in range(2 * p, max_num + 1, p): min_prime[i] = p

    # Aの要素で出てきた素因数をusedに記録
    used = [0] * (max_num + 1)
    for a in A:
        while a > 1:
            p = min_prime[a]
            if used[p]:
                print("setwise coprime")
                return
            while a % p == 0: a //= p
            used[p] = 1
    print("pairwise coprime")




if __name__ == "__main__":
    main()
