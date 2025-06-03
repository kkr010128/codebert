N = int(input())
S = input()

res = ''
for c in S:
    res += chr((ord(c) - ord('A') + N) % 26 + ord('A'))

print(res)