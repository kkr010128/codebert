n = int(input())
s = list(input())
for i in range(len(s)):
    idx = ord(s[i]) - ord('A')
    s[i] = chr((idx + n) % 26 + ord('A'))
print("".join(s))