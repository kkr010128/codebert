s, t = [input() for _ in range(2)]
print('Yes' if s == t[:len(s):] else 'No')