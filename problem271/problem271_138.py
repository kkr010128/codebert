n = int(input())
S = input()
a = ord('A')
z = ord('Z')
ans = ''
for s in S:
    if ord(s) + n <= 90:
        ans += chr(ord(s) + n)
    else:
        ans += chr(a + ord(s) + n - z - 1)
print(ans)
