inp = map(int, raw_input().split())
x = max(inp)
y = min(inp)
while True:
    r = x % y
    x = y
    y = r
    if y == 0:
        break
print x