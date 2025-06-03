a,b = map(int, input().split())
S = 0
for i in range(max(a,b)):
  S +=min(a,b)*(10**i)
print(S)