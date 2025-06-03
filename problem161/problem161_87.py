import sys
input = sys.stdin.readline

def main():

    a,b,n = map(int,input().split())

    if n < b:
        print((a*n)//b)
        exit()

    num = n//b

    ans = (a*(b-1))//b
    print(max(ans,(a*n)//b - a * (n//b)))

if __name__ == '__main__':
    main()
