n = int(input())

S = [False for i in range(13)]
D = [False for i in range(13)]
C = [False for i in range(13)]
H = [False for i in range(13)]


for i in range(n):
    a,b = input().split()
    b = int(b)
    if a == "S":
        S[b-1] = True
    elif a == "D":
        D[b-1] = True
    elif a == "C":
        C[b-1] = True
    elif a == "H":
        H[b-1] = True
        
for i in range(13):
    if S[i] == False:
        print("S "+str(i+1))

for i in range(13):
    if H[i] == False:
        print("H "+str(i+1))
        
for i in range(13):
    if C[i] == False:
        print("C "+str(i+1))
        
for i in range(13):
    if D[i] == False:
        print("D "+str(i+1))