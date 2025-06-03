import sys
import itertools


def main():
    N = int(input())
    songs = []
    time = []
    for _ in range(N):
        s, t = input().split()
        t = int(t)
        songs.append(s)
        time.append(t)
    X = input()
    time = list(itertools.accumulate(time))
    ans = time[-1] - time[songs.index(X)]
    print(ans)


if __name__ == '__main__':
    main()
