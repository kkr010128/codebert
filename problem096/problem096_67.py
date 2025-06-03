#!/usr/bin/env python3
#xy = [map(int, input().split()) for _ in range(5)]
#x, y = zip(*xy)

def main():
    nd = list(map(int, input().split()))
    ans = 0
    for i in range(nd[0]):
        xy = list(map(int, input().split()))
        if xy[0] * xy[0] + xy[1] * xy[1] <= nd[1] * nd[1]:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
