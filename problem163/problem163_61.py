S, W = map(int, input().split())
result = ""

if S <= W:
    result = "unsafe"
else:
    result = "safe"

print(result)
