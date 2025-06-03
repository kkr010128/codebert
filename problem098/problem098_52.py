N = int(input())
C = list(input())

r = C.count("R")

cnt = 0
for i in range(r):
    if C[i] == "W":
        cnt += 1
        
print(cnt)