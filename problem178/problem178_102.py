X,Y,Z = map(int,input().split())

temp = Y
Y = X
X = temp

temp = Z
Z = X
X = temp

print ("{} {} {}".format(X,Y,Z))