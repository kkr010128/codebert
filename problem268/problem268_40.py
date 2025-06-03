N = int(input())
A = list(map(int,input().split()))

R, B, G = 0, 0, 0
ans = 1

for a in A:
    if R == a:
        if B == a and G == a:
            ans *= 3
        elif B == a or G == a:
            ans *= 2
        else:
            ans *= 1
        R += 1
    elif B == a:
        if G == a:
            ans *= 2
        else:
            ans *= 1
        B += 1
    elif G == a:
        ans *= 1
        G += 1
    else:
        print(0)
        exit()
    
    ans %= 10**9+7

print(ans)