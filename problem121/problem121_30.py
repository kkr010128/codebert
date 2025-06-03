N = int(input().strip())

ans = ''
while N > 0:
    ans = chr(ord('a') + (N-1) % 26) + ans
    N = (N -1) // 26

print(ans)
