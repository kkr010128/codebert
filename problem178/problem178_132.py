X,Y,Z = map(int,input().split())
G = X
X = Y
Y = G
G = X
X = Z
Z = G
print(f'{X} {Y} {Z}')
