N = int(input())
li = list(map(int, input().split()))
minL = 2 * (10**6)
count = 0
for l in li:
  if (minL >= l):
    count += 1
    minL = l
print(count)