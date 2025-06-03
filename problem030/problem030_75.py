import math

a, b, degC = [ float( i ) for i in raw_input( ).split( " " ) ]
radC = degC*math.pi/ 180.0
h = math.sin( radC ) * b
S = (a*h)/2
x = math.cos( radC ) * b
x -= a
c = math.sqrt(  x**2 + h**2  ) 
L = a + b + c

print( S )
print( L )
print( h )