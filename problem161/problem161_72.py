import sys
def input(): return sys.stdin.readline().rstrip()
 
 
def main():
    a,b,n=map(int, input().split())
    if b<=n:
        n=b-1
    print(((a*n)//b) - (a*(n//b)))
    

    
 
if __name__ == '__main__':
    main()