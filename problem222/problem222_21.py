N = int(input())
A = list(map(int,input().split()))
A.sort()

check = True
for i in range(N-1):
  if A[i] == A[i+1]:
    check = False
    
print("YES" if check else "NO")