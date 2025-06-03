import collections
#nを素因数分解したリストを返す
def prime_decomposition(n):
  i = 2
  table = []
  while i * i <= n:
    while n % i == 0:
      n //= i
      table.append(i)
    i += 1
  if n > 1:
    table.append(n)
  return table

N = int(input())
if N == 1:
    print(0)
else:
    A = prime_decomposition(N)

    c = collections.Counter(A)
    values, counts = zip(*c.most_common())


    cnt = 0
    for i in range(len(counts)):
        for j in range(10,0,-1):
            if counts[i] >= j * (j + 1)//2:
                cnt += j
                break
    print(cnt)