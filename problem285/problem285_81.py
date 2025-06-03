S = input().replace("><", "> <").split()
ans = 0
for s in S:
    up = s.count("<")
    down = len(s) - up
    if up < down: 
        up -= 1
        ans += up * (up+1) // 2 + down * (down+1) // 2
    else:
        down -= 1
        ans += up * (up+1) // 2 + down * (down+1) // 2
print(ans)