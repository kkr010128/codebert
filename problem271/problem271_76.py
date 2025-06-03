n = int(input())
s = input()
ans = ''

for i in range(len(s)):
    next = ord(s[i]) + n
    if next > ord('Z'):
        next -= 26
    ans += (chr(next))

print(ans)