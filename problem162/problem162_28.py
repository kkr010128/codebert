def resolve():
    N, M = map(int, input().split())
    if N%2==1:
        for i in range(1, M+1):
            a, b = i, N-i
            print(a, b)
    else:
        for i in range(1, M+1):
            a, b = i, N - i
            # 円として配置したとき、b-aが半分以上になったら片方だけ進める
            if b-a <= N//2:
                a += 1
            print(a, b)

if __name__ == "__main__":
    resolve()
