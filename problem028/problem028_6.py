N, M = map(int, input().split())
A = list(map(int, input().split()))
memory = [10**6 for _ in range(N + 1)]
flg = [False for _ in range(N + 1)]
memory[0] = 0
flg[0] = True
for a in A:
  m = 0
  while m < len(memory) and m + a < len(memory):
    if flg:
      memory[m + a] = min(memory[m] + 1, memory[m + a])
      flg[m + a] = True
    m += 1
print(memory[-1])
