s = input()

def addAll(end):
  return (end * (end + 1)) // 2

total = 0
index = 0

while len(s) > index:
  leftCount = 0
  rightCount = 0
  while len(s) > index and s[index] == "<":
    leftCount += 1
    index += 1
  while len(s) > index and s[index] == ">":
    rightCount += 1
    index += 1
  maxCount = max(leftCount, rightCount)
  minCount = min(leftCount, rightCount)
  total += addAll(maxCount) + addAll(max(minCount - 1, 0))

print(total)