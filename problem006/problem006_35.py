import sys
import math

def main():
    n = int(input().rstrip())
    r = 1.05
    digit = 3
    a = 100000
    
    for i in range(n):
        a = math.ceil(a*r/10**digit)*10**digit

    print(a)
    
if __name__ == '__main__':
    main()