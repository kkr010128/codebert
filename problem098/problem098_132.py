n = int(input())
stone = list(input())
l = 0
r = n-1
ans = 0
while l < r:
    if stone[l]=='W':
        if stone[r]=='R':
            ans += 1
            l += 1
            r -= 1
        else:
            r -= 1
    else:
        l += 1
        if stone[r]=='W':
            r -= 1
print(ans)