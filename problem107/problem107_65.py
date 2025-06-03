N = int(input())
X = input()

def popcnt1(n):
    return bin(n).count("1")

k = [0,1,1,2,1,2,1,2,1,2,1,2,1,2,2,3,1,2,1] #18まで

c = 0
for i in range(N):
    if X[i] == "1":
        c += 1

m1 = 0
p1 = 0

for i in range(N):
    if c != 1:
        if X[i] == "1":
            m1 += pow(2,N-1-i,c-1)
            m1 %= c-1
            p1 += pow(2,N-1-i,c+1)
            p1 %= c+1
    else:
        if X[i] == "1":
            p1 += pow(2,N-1-i,c+1)
            p1 %= c+1

for i in range(N):
    if c != 1: 
        if X[i] == "0":
            B2 = p1 + pow(2,N-1-i,c+1)
            B2 %= c+1
        else:
            B2 = m1 - pow(2,N-1-i,c-1)
            B2 %= c-1
    else:
        if X[i] == "0":
            B2 = p1 + pow(2,N-1-i,c+1)
            B2 %= c+1
        else:
            print(0)
            continue

    S = len(bin(B2))
    c2 = popcnt1(B2)

    if c2 == 0:
        print(1)
    else:
        print(2+k[B2%c2])