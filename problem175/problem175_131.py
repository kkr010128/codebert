import sys
input = sys.stdin.readline
import bisect


# 持っているビスケットを叩き、1枚増やす
# ビスケット A枚を 1円に交換する
# 1円をビスケット B枚に交換する
def main():
    n = int(input())
    s = input()
    R, G, B = [], [], []
    for i in range(n):
        index = i+1
        if s[i] == "R":
            R.append(index)
        elif s[i] == "G":
            G.append(index)
        elif s[i] == "B":
            B.append(index)
    all_count = len(R)*len(G)*len(B)
    count = 0
    # j - i != k - j
    # k = 2j - i
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j]:
                continue
            k = 2*j - i
            if k >= n:
                continue
            if s[k] == s[i] or s[k] == s[j]:
                continue
            count += 1
    print(all_count - count)

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
