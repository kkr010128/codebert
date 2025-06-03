n = int(input())

S = [1]*13
H = [1]*13
C = [1]*13
D = [1]*13

mark = [""]*n
num = [""]*n

for i in range(n):
    mark[i], num[i] = input().split()

for i in range(n):
    if mark[i] == "S":
        S[int(num[i])-1] = 0
    if mark[i] == "H":
        H[int(num[i])-1] = 0
    if mark[i] == "C":
        C[int(num[i])-1] = 0
    if mark[i] == "D":
        D[int(num[i])-1] = 0

for i in range(13):
    if S[i]:
        print("S " + str(i+1))
for i in range(13):
    if H[i]:
        print("H " + str(i+1))
for i in range(13):
    if C[i]:
        print("C " + str(i+1))
for i in range(13):
    if D[i]:
        print("D " + str(i+1))