X, Y = [int(arg) for arg in input().split()]

def f(X, Y):
    for i in range(X + 1):
        for j in range(X + 1):
            kame = i
            tsuru = j
            if kame + tsuru == X and kame * 4 + tsuru * 2 == Y:
                return 'Yes'
    return 'No'

print(f(X, Y))