n = int(input())
s = input()
l = 0
r = n - 1
cnt = 0

while l<r:
    while s[l] == 'R' and l < r:
        l += 1
    while s[r] == 'W' and l < r:
        r -= 1
    if l>=r:
        break
    cnt += 1
    l += 1
    r -= 1

print(cnt)
