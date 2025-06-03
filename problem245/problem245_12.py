def solve():
    N = int(input())
    S = input()

    if N != len(S):
        return

    ans = 0
    for i in range(N-2):
        target_segment = S[i:i+3]
        if target_segment == "ABC":
            ans += 1
    print(ans)

if __name__ == "__main__":
    solve()