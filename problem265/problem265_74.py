N = int(input())
X = N // 1.08
result1 = int(X) * 1.08
result2 = (int(X)+1) * 1.08
result3 = (int(X)-1) * 1.08

if int(result1) == N:
  result = int(X)
elif int(result2) == N:
  result = int(X) + 1
elif int(result3) == N:
  result = int(X) -1
else:
  result = ':('

print(result)