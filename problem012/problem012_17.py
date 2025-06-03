import math


def main():
    n = int(input())
    ans = 0
    for i in range(n):
        x = int(input())
        if x == 2:
            ans += 1
        elif x % 2 == 0:
            pass
        else:
            flag = True
            j = 3
            while j <= math.sqrt(x):
                if x % j == 0:
                    flag = False
                    break
                j += 2
            if flag:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
