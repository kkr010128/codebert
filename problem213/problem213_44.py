N = int(input())
X = list(map(int, input().split()))
count = 0
ave = round(sum(X) / len(X))

for i in X:
  count += (i - ave)**2

print(count)