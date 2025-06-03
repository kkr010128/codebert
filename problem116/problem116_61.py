def main(S, T):
    N = len(S)
    ans = 0
    for i in range(N//2):
        if S[i] != T[i]:
            ans += 1
        if S[-1-i] != T[-1-i]:
            ans += 1
    if N%2 == 1:
        if S[N//2] != T[N//2]:
            ans += 1
    return ans

if __name__ == '__main__':
    S = input()
    T = input()
    ans = main(S, T)
    print(ans)

