X,Y,Z = (int(X) for X in input().split())
Y,X = X,Y
Z,X = X,Z
print('{} {} {}'.format(X,Y,Z))