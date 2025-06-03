n = int(input())
s = input()
counter = 0
for i in range(n):
  j = i +3
  if j > n:
    break
  if s[i:j] == 'ABC':
    counter += 1
print(counter)