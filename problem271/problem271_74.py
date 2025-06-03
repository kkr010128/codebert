n = int(input())
s = list(input())
ans = []
for i in range(len(s)):
    a = ord(s[i])
    moji = a + n if a + n <= 90 else a + n -26
    ans += [chr(moji)]
print("".join(ans))