def euclideanAlgorithm(x, y):
    if y == 0: return x
    return euclideanAlgorithm(y, x%y)

# MAIN
x, y = map(int, raw_input().split())
print euclideanAlgorithm(x, y)