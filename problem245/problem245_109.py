N = int(input())
S = list(input())
check = 0
for i in range(N-1):
  if S[i] != "*":
    if S[i:i+3] == ["A","B","C"]:
      check += 1
      S[i:i+3] = ["*"]*3
print(check)