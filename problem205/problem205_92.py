def main():
    N,P = map(int,input().split())
    S = input()[::-1]
    ans = 0
    if P == 2 or P == 5:
        for i,s in enumerate(S):
            if int(s) % P == 0:
                ans += N - i
    else:
        mods = [0] * P
        mods[0] = 1
        current = 0
        x = 1
        for s in S:
            current = (current + x * int(s)) % P
            ans += mods[current % P]
            mods[current % P] += 1
            x = x * 10 % P
    print(ans)

if __name__ == '__main__':
    main()