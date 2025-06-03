# coding: utf-8


def main():
    A, B = map(int, input().split())
    ans = -1
    for i in range(10001):
        if i * 8 // 100 == A and i // 10 == B:
            ans = i
            break

    print(ans)

if __name__ == "__main__":
    main()
