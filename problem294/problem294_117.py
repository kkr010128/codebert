import bisect
n = int(input())
lines = list(int(i) for i in input().split())
lines.sort()
counter = 0

for i in range(n-2):
  for j in range(i+1, n-1):
    counter += bisect.bisect_left(lines, lines[i] + lines[j]) - (j + 1)
    
print(counter)