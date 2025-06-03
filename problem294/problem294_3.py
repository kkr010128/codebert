import sys
input = sys.stdin.readline
import collections
import bisect

def main():
    n = int(input())
    l = input_list()
    l.sort()
    ans = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            ind = bisect.bisect_left(l, l[i]+l[j])
            num = ind - 1 - j
            ans += num
    print(ans)


def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


if __name__ == "__main__":
    main()
