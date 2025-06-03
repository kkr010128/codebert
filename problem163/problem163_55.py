# -*- coding: utf-8 -*-

def main():

    S, W = map(int, input().split())

    if S <= W:
        ans = 'unsafe'

    else:
        ans = 'safe'

    print(ans)


if __name__ == "__main__":
    main()