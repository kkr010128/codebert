n = int(input())
A = [None] * n
for i in range(n):
  A[i] = int(input())

def insertionSort(A, n, g):
  cnt = 0
  for i in range(g, n, 1):
    # Insertion Sort
    # e.g. if g == 4 and i == 8:  [4] 6  2  1 [10] 8  9  5 [3] 7
    j = i - g  # e.g. j = 4
    k = i      # e.g. k = 8
    while j >= 0 and A[j] > A[k]:
      #print("i:{} j:{} k:{} A:{}".format(i, j, k, A))
      A[j], A[k] = A[k], A[j]
      k = j       # e.g. k = 4
      j = k - g   # e.g. j = 4 - 0 = 0
      cnt += 1
      #print("j reduced to {}, k reduced to {}".format(j, k))

  return(cnt)

def shellSort(A, n):
  g = [0]
  m = 0
  sum = 0
  while True:
    if (3*m + 1 <= n):
      g.insert(0, 3*m + 1)
      m = 3*m + 1
    else:
      break
  
  for i in range(len(g)):
    cnt = insertionSort(A, n, g[i])
    sum += cnt

  print(len(g))
  print(str(g).replace('[', '').replace(']', '').replace(',', ''))
  print(sum)
  for i in range(n):
    print(A[i])

def main():
  shellSort(A, n)

main()

