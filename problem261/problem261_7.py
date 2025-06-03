str = input()
n = int(len(str) / 2)
cnt = 0
for i in range(n):
  if str[i] != str[-1-i]:
    cnt += 1

print(cnt)