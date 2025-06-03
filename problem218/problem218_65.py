import collections
import sys
input = sys.stdin.readline


def main():
    N = int(input())
    S = [input().rstrip() for _ in range(N)]
    c = collections.Counter(S).most_common()
    max_freq = None
    max_S = []
    for s, freq in c:
        if max_freq is None:
            max_freq = freq
            max_S.append(s)
        elif freq == max_freq:
            max_S.append(s)
        else:
            break
    print('\n'.join(sorted(max_S)))


if __name__ == "__main__":
    main()
