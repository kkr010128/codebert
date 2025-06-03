def solve():
    N, P = map(int, input().split())
    S = input()

    if P == 2 or P == 5:
        res = 0

        for i in range(N):
            if int(S[i]) % P == 0:
                res += i + 1
        
        print(res)

    else:
        res = 0
        count = [0] * P
        r = 0

        for i in range(N-1, -1, -1):
            r = (int(S[i]) * pow(10, N-1 - i, P) + r) % P
            if r == 0: res += 1
            res += count[r]
            count[r] += 1
        
        print(res)

if __name__ == '__main__':
    solve()
