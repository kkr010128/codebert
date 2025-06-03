A,B,C,D= map(int, input().split())
while (True):
    C = C - B
    if ( C <= 0 ):
        result = "Yes"
        break
    A = A - D
    if ( A <= 0 ) :
        result = "No"
        break
print ( result )
