N = int(input())
A = list(map(int, input().split()))
counter = [0 for _ in range(max(A)+1)]
appeard = []
for k in range(N):
  counter[A[k]] += 1
  if counter[A[k]] == 2:
    appeard.append(A[k])

allsum = 0
for item in appeard:
  allsum += counter[item]*(counter[item]-1)//2
for k in range(N):
  if counter[A[k]] > 1:
    print(allsum - (counter[A[k]]-1))
  else:
    print(allsum)