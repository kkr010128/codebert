H = int(input())
count = 0
answer = 0
while(H > 1):
  H //= 2
  answer += 2**count
  count += 1
answer += 2**count
print(answer)