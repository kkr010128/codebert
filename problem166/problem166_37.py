import sys
input = sys.stdin.readline

def main():
    s = input().strip()
    mod = [0] * 2019

    tmp = 0
    ten = 10
    mod[tmp] += 1
    for i in range(len(s)-1, -1, -1):
        tmp = (tmp + ten * int(s[i])) % 2019
        ten = (ten * 10) % 2019
        mod[tmp] += 1
    ans = 0
    for i in range(2019):
        if mod[i] > 1:
            ans += (mod[i] * (mod[i] - 1)) // 2
    print(ans)


if __name__ == "__main__":
    main()