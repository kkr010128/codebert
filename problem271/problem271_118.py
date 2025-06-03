N = int(input())
S = input()

plus = N % 26
result = ''
for c in S:
    next = ord(c) + plus
    result += chr(next - 26) if next > 90 else chr(next)
print(result)
