s, w = list(map(int, input().split()))
output = "safe"
if s <= w:
  output = "un" + output
print(output)