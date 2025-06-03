n,m,q = [int(_) for _ in input().split()]
a = []
b = []
c = []
d = []

for q in range(q):
  tmplist = [int(_) for _ in input().split()]
  a.append(tmplist[0])
  b.append(tmplist[1])
  c.append(tmplist[2])
  d.append(tmplist[3])

# Aという数列を再帰関数で求める
# {} → {A1, A2, A3...AN} の数

result=[]
def score(A):
  max_score = 0
  for i in range(q+1):
    if A[b[i]-1] - A[a[i]-1] != c[i]: # なぜマイナス１をしているのか？：ｑ
      continue
    else:
      max_score+= d[i]
  return max_score

def dfs(A):
  if len(A) == n+1: # 配列の個数はN個
    return score(A)
  result = 0
  past_data = A[-1]
  for v in range(past_data,m+1):
    A.append(v)
    result = max(result,dfs(A))
    A.pop()
  return result

print(dfs([1]))
