import sys
input = sys.stdin.readline
import collections


def main():
    N = int(input())
    A = list(map(int, input().split()))
    v_freq = collections.Counter(A)
    v_sum = 0
    for v, freq in v_freq.items():
        v_sum += v * freq
    Q = int(input())
    for _ in range(Q):
        B, C = map(int, input().split())
        if B in v_freq:
            v_sum -= (B - C) * v_freq[B]
            if C in v_freq:
                v_freq[C] += v_freq[B]
            else:
                v_freq[C] = v_freq[B]
            del v_freq[B]
            print(v_sum)
        else:
            print(v_sum)


if __name__ == '__main__':
    main()
