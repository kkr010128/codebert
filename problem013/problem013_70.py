n = int(input())
DifMax = -9999999999999

R = [int(input())]
RMin = R[0]
for i in range(1, n):
  if RMin > R[i-1]:
      RMin = R[i-1]
  R.append(int(input()))
  if DifMax < R[i] - RMin:
    DifMax = R[i] - RMin

print(DifMax)