# coding: utf-8

def main():
    N = input()
    X = list(map(int, input().split()))
    ans = 1000001

    for i in range(1, 101):
        tmp = sum([(x - i) ** 2 for x in X])
        if tmp < ans:
            ans = tmp

    print(ans)

if __name__ == "__main__":
    main()
