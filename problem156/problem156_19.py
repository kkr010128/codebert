# D - I hate Factorization
M = 1000
N = [0]
for i in range(1,M+1):
    N.append(i)
    N.append(-i)

def main(X):
    global N
    for i in N:
        for j in N:
            if i**5-j**5==X:
                return i,j

X = int(input())
A,B = main(X)
print(A,B)