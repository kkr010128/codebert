import sys
input = sys.stdin.readline

def main():
    n , k = map( int , input().split() )
    A = [ 0 for i in range(n) ]
    for i in range(k):
        d = int(input())
        a = list( map( int , input().split() ) )
        for j in a:
            A[ j - 1 ] += 1

    ans = 0
    for i in A:
        if i == 0:
            ans += 1

    print(ans)

main()