# D - Alter Altar
N = int(input())
c = input()
white_l = 0
red_r = 0
for i in range(N):
    if c[i]=='R':
        red_r += 1
ans = red_r
for i in range(N):
    if c[i]=='W':
        white_l += 1
    else:
        red_r -= 1
    ans = min(ans, max(red_r,white_l))
print(ans)