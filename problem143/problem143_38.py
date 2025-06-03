# -*- coding: utf-8 -*-

def main():

    K = int(input())
    S = input()

    if len(S) <= K:
        ans = S

    else:
        ans = S[:K] + '...'

    print(ans)


if __name__ == "__main__":
    main()