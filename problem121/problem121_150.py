N = int(input())

ans = ""

while N > 0:
    N -= 1
    N, digit = divmod(N, 26)
    ans += chr(ord('a') + digit)
print(ans[::-1])