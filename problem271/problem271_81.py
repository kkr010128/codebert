N = int(input())
S = input()
ans = ''
for c in S:
    i = ord(c) - ord('A')
    ans += chr(ord('A') + (i+N)%26)
print(ans)