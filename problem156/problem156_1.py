def calc(X):
    A = 1
    B = 1
    if X == 0:
        return A,B
    else:
        l_bound = 1
        h_bound = 200
        for i in range(l_bound,h_bound):
            for j in range(0,i+1):
                if i ** 5 - j ** 5 == X:
                    A = i
                    B = j
                    return A,B
                if i ** 5 + j ** 5 == X:
                    A = i
                    B = -j
                    return A,B
def resolve():
    X = int(input())
    A,B = calc(X)  
    print(str(A) + " " + str(B))
resolve()