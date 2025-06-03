n = int(input())
s = [input() for _ in range(n)]

uniq = set(s)
print(len(uniq))