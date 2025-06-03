def main():
    x, y, a, b, c = list(map(int, input().split()))
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    R = list(map(int, input().split()))
    P = sorted(P, reverse = True)[:x]
    Q = sorted(Q, reverse = True)[:y]
    ans = sorted(P + Q + R, reverse = True)
    print(sum(ans[:x + y]))

if __name__ == '__main__':
    main()
