s = input()
ans = [i.upper() if 'a' <= i <= 'z' else i.lower() if 'A' <= i <= 'Z' else i for i in s[:]]
print(*ans, sep='')
