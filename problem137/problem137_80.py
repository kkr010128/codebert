N = int(input())
A = [0]*N
B = [0]*N
for i in range(N): A[i],B[i] = map(int,input().split())
A.sort()
B.sort()

sorted_A = A
sorted_B = B

if N % 2 != 0:
  center_A = sorted_A[N//2]
  center_B = sorted_B[N//2]
  print(center_B - center_A + 1)
else:
  center_A = (sorted_A[N//2-1] + sorted_A[N//2]) / 2
  center_B = (sorted_B[N//2-1] + sorted_B[N//2]) / 2
  print(int((center_B - center_A)*2 + 1))