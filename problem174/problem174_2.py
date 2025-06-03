import sys
import math
input = sys.stdin.readline

def main():
    k = int(input())
    ans = 0

    for a in range( 1 , k+1 ):
        for b in range( a , k+1 ):
            x = math.gcd( a , b )
            for c in range( b , k+1 ):
                y = math.gcd( x , c )
                if a == b == c:
                    ans += y
                elif a==b or b==c or c==a:
                    ans += 3 * y
                else:
                    ans += 6 * y

    print(ans)



main()