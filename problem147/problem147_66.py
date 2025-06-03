# -*- coding: utf-8 -*-

def main():

    S = input()
    T = input()

    if S == T[:len(S)]:
        ans = 'Yes'

    else:
        ans = 'No'

    print(ans)


if __name__ == "__main__":
    main()