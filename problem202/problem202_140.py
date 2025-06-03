# coding: utf-8

def main():
    N, A, B = map(int, input().split())
    quo = N // (A + B)
    rem = N % (A + B)

    if (rem > A): rem = A
    ans = quo * A + rem

    print(ans)

if __name__ == "__main__":
    main()
