n,k = map(int, input().split())
r, s, p = map(int, input().split())
T = list(str(input()))
ans = 0
S = [-1]*n
for i in range(n):
    if i <= k-1:
        if T[i] == 'r':
            S[i] = 'p'
            ans += p
        elif T[i] == 's':
            S[i] = 'r'
            ans += r
        else:
            S[i] = 's'
            ans += s
    else:
        if T[i] == 'r':
            if S[i-k] != 'p':
                S[i] = 'p'
                ans += p
            else:
                if i+k <= n-1:
                    if T[i+k] == 's':
                        S[i] = 's'
                    elif T[i+k] == 'p':
                        S[i] = 'r'
                    else:
                        S[i] = 'r'
                else:
                    S[i] = 'r'
        elif T[i] == 's':
            if S[i-k] != 'r':
                S[i] = 'r'
                ans += r
            else:
                if i+k <= n-1:
                    if T[i+k] == 'p':
                        S[i] = 'p'
                    elif T[i+k] == 'r':
                        S[i] = 's'
                    else:
                        S[i] = 's'
                else:
                    S[i] = 's'
        else:
            if S[i-k] != 's':
                S[i] = 's'
                ans += s
            else:
                if i+k <= n-1:
                    if T[i+k] == 's':
                        S[i] = 'p'
                    elif T[i+k] == 'r':
                        S[i] = 'r'
                    else:
                        S[i] = 'p'
                else:
                    S[i] = 'p'
print(ans)
