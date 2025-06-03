n = int(input())
R =[]
for i in range(n):
 R.append(int(input()))

maxR = R[1]
minR = R[0]
maxB = R[1] - R[0]
for i in range(1,n):
 if R[i] < minR:
  minR = R[i]
  maxR = R[i] - 1
 elif minR <= R[i] and R[i] <= maxR:
  continue
 else:
  maxR = R[i]
  if maxR - minR > maxB:
   maxB = maxR - minR

print(str(maxB))