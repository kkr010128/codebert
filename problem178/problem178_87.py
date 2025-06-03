XYZ = list(map(int, input().split()))
ABC = [0]*3
for i in range(3):
  ABC[i] = XYZ[(i+2)%3]
print(" ".join(map(str,ABC)))