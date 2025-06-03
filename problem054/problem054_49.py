n = int(input())
S = []
C = []
H = []
D = []
for i in range(1, 14):
    S.append(i)
    C.append(i)
    H.append(i)
    D.append(i)
for i in range(n):
    s = input().split(" ")
    if s[0] == "S":
        S.remove(int(s[1]))
    elif s[0] == "C":
        C.remove(int(s[1]))
    elif s[0] == "H":
        H.remove(int(s[1]))
    else:
        D.remove(int(s[1]))
for i in range(len(S)):
    print("S {0}".format(S[i]))
for i in range(len(H)):
    print("H {0}".format(H[i]))
for i in range(len(C)):
    print("C {0}".format(C[i]))
for i in range(len(D)):
    print("D {0}".format(D[i])) 