n = int(input())
s = input()
ans = ""

for i in range(len(s)):
    x = ord(s[i]) - ord('A') + n
    ans += chr(x % 26 + ord('A'))
print(ans)
