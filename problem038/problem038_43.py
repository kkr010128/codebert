a, b = map(int, input().split())
op = "=="
if a < b: op = "<"
if a > b: op = ">"
print("a %s b" % op)