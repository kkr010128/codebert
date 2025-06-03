import sys
input = sys.stdin.readline
import collections

# 持っているビスケットを叩き、1枚増やす
# ビスケット A枚を 1円に交換する
# 1円をビスケット B枚に交換する
def main():
    x = int(input())
    for a in range(-200, 200):
        for b in range(-200, 200):
            ans = a ** 5 - b ** 5
            if ans == x:
                print(a, b)
                exit()


def bi(num, a, b, x):
    print((a * num) + (b * len(str(b))))
    if (a * num) + (b * len(str(b))) <= x:
        return False
    return True

def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


if __name__ == "__main__":
    main()
