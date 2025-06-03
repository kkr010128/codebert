N = int(input())

multiplication = []
for x in range(1, 10):
    for y in range(1, 10):
        multiplication.append(x*y)

if N in multiplication:
    print( "Yes" )
else:
    print( "No" )