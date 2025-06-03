NXT = [int(i) for i in input().split(' ')]
import math
T_total = ( math.ceil( NXT[0]/ NXT[1] )*NXT[2] )

print (T_total)