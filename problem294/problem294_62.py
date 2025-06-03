N = int(input())
L = list(map(int,input().split()))
L = sorted(L)

def binary_search(a,b):
  top = N
  bottom = b
  c = (top + bottom)//2
  while top - bottom > 1:
    #print(a,b,":",top,bottom,c)
    if L[c] < L[a] + L[b]:
      bottom = c
    else:
      top = c
    c = (top + bottom)//2
  return top - 1

cnt = 0
for a in range(N-2):
  for b in range(a+1,N-1):
    cnt += binary_search(a,b) - b

print(cnt)