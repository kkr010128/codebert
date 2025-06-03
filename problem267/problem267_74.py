#!/usr/bin/env python3
def main():
    N = int(input())
    S = input()

    seen = set()
    ans = 0
    for i in range(N - 2):
        if S[i] in seen:
            continue
        seen.add(S[i])
        for j in range(i + 1, N - 1):
            if S[i] + S[j] in seen:
                continue
            seen.add(S[i] + S[j])
            for k in range(j + 1, N):
                if S[i] + S[j] + S[k] in seen:
                    continue
                seen.add(S[i] + S[j] + S[k])
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
