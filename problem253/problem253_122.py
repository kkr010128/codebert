def main():
    N, A, B = map(int, input().split())
    diff = abs(A-B)
    if diff%2 == 0:
        ans = diff//2
    else:
        # 端に行く
        # 一回端のままになる => 偶数のときと同じ
        ans = min(A-1, N-B)
        diff -= 1; ans += 1
        ans += diff//2
    print(ans)

if __name__ == "__main__":
    main()
