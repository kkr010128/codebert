H =int(input())

#h= 1
#while 2**(h+1) <= H:
#    h += 1
#
#n=2**(h+1) - 1
#print(n)
#
import math
def helper(h):
    if h ==1:
        return 1
    return 1 + 2 * helper(math.floor(h/2))
print(helper(H))