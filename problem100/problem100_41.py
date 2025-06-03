X = int(input())

def define_rate(X):
    if X >= 1800:
        return 1
    elif X >= 1600:
        return 2
    elif X >= 1400:
        return 3
    elif X >= 1200:
        return 4
    elif X >= 1000:
        return 5
    elif X >= 800:
        return 6
    elif X >= 600:
        return 7
    elif X >= 400:
        return 8

print(define_rate(X))