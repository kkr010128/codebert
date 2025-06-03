A = []
A.append(input().split())
A.append(input().split())
A.append(input().split())
N = int(input())
b = [input() for _ in range(N)]
 
# 2次元配列として処理
for i in range(N):
  for j in range(3):
    if b[i] in A[j]: A[j][A[j].index(b[i])] = True

if (A[0][0]==True and A[1][0]==True and A[2][0]==True) or (A[0][1]==True and A[1][1]==True and A[2][1]==True) or (A[0][2]==True and A[1][2]==True and A[2][2]==True) or (A[0][0]==True and A[0][1]==True and A[0][2]==True) or (A[1][0]==True and A[1][1]==True and A[1][2]==True) or (A[2][0]==True and A[2][1]==True and A[2][2]==True) or (A[0][0]==True and A[1][1]==True and A[2][2]==True) or (A[0][2]==True and A[1][1]==True and A[2][0]==True): print('Yes')
else: print('No')