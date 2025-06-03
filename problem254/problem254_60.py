a = int(input())
b = int(input())
num = [a, b]
for i in range(1, 4):
  if i not in num:
    print(i)
    break