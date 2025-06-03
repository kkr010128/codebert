def rec(a,b):
    return a*b,(a+b)*2
S = input()
X = S.split()
a = int(X[0])
b = int(X[1])

area,perimeter = rec(a,b)
print("{} {}".format(area,perimeter))
