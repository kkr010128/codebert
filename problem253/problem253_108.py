def main():
    from sys import stdin
    n,a,b = map(int,stdin.readline().rstrip().split())
    k = b-a-1
    if k%2==1:
        print(k//2+1)
    else:
        print(k//2+1+min(n-b,a-1))
main()