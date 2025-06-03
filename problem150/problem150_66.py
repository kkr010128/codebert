N, K = map(int ,input().split())
A = [int(x) for x in input().split()]
checked = [False] * N
root=[0]

idx = 0
checked[0]=True

for k in range(K):
  root.append(A[idx]-1)
  idx = A[idx]-1
  if (checked[idx]):
    break
  checked[idx]=True
else:
  print(idx+1)
  exit(0)

for i, r in enumerate(root):
  if r == root[-1]:
    break

root2=root[i:]
l = len(root2)-1
idx = root2[(K-i)%(l)]
print(idx+1)
