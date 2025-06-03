if __name__ == "__main__":
    N = int(input())
    mod = N % 1000
    q = N // 1000
    if mod != 0:
        q += 1
    ans = 1000 * q - N
    print(ans)