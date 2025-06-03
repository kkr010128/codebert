def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if k % 2 == 1:
        x = abs(x-d)
        k -= 1
    if x > d*k:
        print(x-d*k)
    else:
        print(min(x % (2*d), abs(x % (2*d)-2*d)))


main()
