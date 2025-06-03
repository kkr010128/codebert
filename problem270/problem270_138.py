# -*- coding: utf-8 -*-

def main():

    S = input()

    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

    for i, name in enumerate(week):
        if name == S:
            ans = 7 - i

    print(ans)


if __name__ == "__main__":
    main()