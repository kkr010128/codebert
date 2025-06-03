N = int(input())
check = [0, 0, 0]
for i in range(N):
  str = input().split()
  check[i%3] = 1 if str[0] == str[1] else 0
  if sum(check) == 3:
    break
print('Yes') if sum(check) == 3 else print('No')