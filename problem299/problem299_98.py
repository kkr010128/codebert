N = int(input())
list = input().split()
answer = [0] * N

for i in range(N):
  answer[int(list[i]) - 1] = str(i + 1)

print(' '.join(answer))
