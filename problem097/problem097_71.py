
K = int(input())


if K % 2 == 0:
    print(-1)

else:
    seen = set()
    ans = 1
    num = 7
    while ans <= K:

        mod = num % K
        if mod in seen:
            ans = -1
            break
        else:
            seen.add(mod)
        
        if mod == 0:
            break
        else:
            num = mod * 10 + 7
            ans += 1
    
    print(ans)

