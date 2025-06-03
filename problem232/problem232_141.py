a, b = map(int, input().split())

ab = str(a) * b
ba = str(b) * a

print(sorted([ab, ba])[0])
