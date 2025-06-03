X = int(input())


def f(X):

    for A in range(-118, 120):
        for B in range(-119, 119):
            if A**5-B**5 == X:
                print(A,  B)
                exit()


f(X)
