X , Y , Z = map(int,input().split())
tmp = 0

tmp = X
X = Y
Y = tmp

tmp = X
X = Z
Z = tmp

print( str( X ) + " " + str( Y ) + " " + str( Z ) )