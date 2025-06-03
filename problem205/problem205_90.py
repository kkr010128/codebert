
def main():
    N, P = map(int, input().split())
    S = input()
    ans = 0
    mods = [0 for i in range(N+1)]
    digits = 1

    if P == 2 or P == 5:
        for i in range(N-1, -1, -1):
            if int(S[i])%P == 0:
                ans += i+1
        print(ans)
        return

    for i in range(N-1, -1, -1):
        mods[i] = (int(S[i]) * digits % P + mods[i+1]) % P
        digits = digits * 10 % P

    count = [0 for i in range(P)]
    for i in range(N, -1, -1):
        ans += count[mods[i]]
        count[mods[i]] += 1

    print(ans)

main()