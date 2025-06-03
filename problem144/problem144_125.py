from math import cos , sin, sqrt, radians
import sys

A , B , H , M = list( map( int, input().split() ) )

th1 = H * 30 + 0.5 * M
th2 = M * 6

theta = min( abs( th1 - th2 ) , 360 - abs( th1 - th2 ))
if theta == 180.0:
    print(A+B)
    sys.exit()
theta = radians(theta)
ans = sqrt( (B * sin(theta))**2 + ( B*cos(theta) - A )**2 )
print(ans)