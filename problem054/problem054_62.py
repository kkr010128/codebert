n = int(raw_input())
temp = ''
S = ['S']
D = ['D']
H = ['H']
C = ['C']

for i in range(n):
    temp = str(raw_input())
    if temp[0] == 'S':
        S.append(temp)
    elif temp[0] == 'H':
        H.append(temp)
    elif temp[0] == 'C':
        C.append(temp)
    elif temp[0] == 'D':
        D.append(temp)

def find(X):
    frag = 0
    for i in range(1, 14):
        for j in range(1, len(X)):
            if X[j] == X[0][0] + ' ' + str(i):
                frag = 1
                break
        if frag == 0:
            print X[0][0] + ' ' + str(i)
        frag = 0

find(S)
find(H)
find(C)
find(D)