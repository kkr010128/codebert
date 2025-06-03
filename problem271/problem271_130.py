N = int(input())
S = input()

ans = ''
for i in S:
    num = (ord(i) + N)
    if num > 90:
        num = 64 + num % 90
    ans += chr(num)

print(ans)
