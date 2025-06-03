X, K, D = (int(x) for x in input().split())

if X > 0:
    div, mod = divmod(X, D)
    if div >= K:
        answer = X - K*D
    else:
        if (K - div)%2 == 0:
            answer = X - div*D
        else:
            answer = abs(X - (div+1)*D)
elif X < 0:
    div, mod = divmod(-X, D)
    if div >= K:
        answer = abs(X + K*D)
    else:
        if (K - div)%2 == 0:
            answer = abs(X + div*D)
        else:
            answer = X + (div+1)*D
else:
    if K%2 == 0:
        answer = 0
    else:
        answer = D

print(answer)
