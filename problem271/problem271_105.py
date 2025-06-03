N = int(input())
S = input()
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = ""
for s in S:
  i = alpha.index(s)
  result += alpha[i+N]
print(result)