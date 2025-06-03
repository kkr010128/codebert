import math

def main():
    a, b, n = map(int, input().split())
    x = n if (b-1) > n else b-1
    print(math.floor(a*x/b)-a*math.floor(x/b))
         
if __name__ == '__main__':
    main()