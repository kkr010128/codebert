N = int(input()) - 1
rst = ''
for i in range(1, 10 ** 15):
    if N >= 26 ** i:
        N -= 26 ** i
        continue
    for j in range(i):
        rst += chr(ord('a') + N % 26)
        N //= 26
    print(rst[::-1])
    break