import sys

def merge(A, left, mid, right):
  n1 = mid - left
  n2 = right - mid
  L = []
  R = []
  
  global count
  
  for i in range(n1):
    L.append(A[left + i])
  for i in range(n2):
    R.append(A[mid + i])
  L.append('INFTY')
  R.append('INFTY')
  
  a = 0
  b = 0
  
  for k in range(left, right):
    if L[a] <= R[b]:
      A[k] = L[a]
      a += 1
    else:
      A[k] = R[b]
      b += 1
    count += 1

def mergeSort(A, left, right):
  if left + 1 < right:
    mid = (left + right) / 2
    mergeSort(A, left, mid)
    mergeSort(A, mid, right)
    count = merge(A, left, mid, right)


n = sys.stdin.readline()
n = int(n)


count = 0

data = sys.stdin.readline()
data_list = data.split(" ")

for i in range(n):
  data_list[i] = int(data_list[i])

mergeSort(data_list, 0, n)

for i in range(n):
  data_list[i] = str(data_list[i])

print " ".join(data_list)
print count