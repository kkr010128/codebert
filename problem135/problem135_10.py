import math
A, B = map(str,input().split(" "))
B_ = int(B.split(".")[0])*100 + int(B.split(".")[1])

print(int(A) * B_ // 100)

