s = input()
small = 'abcdefghijklmnopqrstuvwxyz'
large = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = ''
for i in s:
    q = 0
    while q < 26:
        if i == small[q]:
            ans += large[q]
            break
        elif i == large[q]:
            ans += small[q]
            break
        q += 1
    if q == 26:
        ans += i
print(ans)
