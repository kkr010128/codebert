n = input()

R = [input() for i in range(n)]
  
max = R[1] - R[0]
min = R[0]
  
for i in range(1,n):
    if R[i] - min > max:
        max = R[i] - min
    if R[i] < min:
        min = R[i]
  
print max