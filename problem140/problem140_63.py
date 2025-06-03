T = input()
T = ['D' if c == '?' else c for c in T]
print(*T, sep='')