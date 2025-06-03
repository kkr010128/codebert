import math
def main():
    n,m = map(int,input().split())
    a = list(map(int,input().strip().split()))
    
    if n >= sum(a):
        print(n-sum(a))
        return 
    else:
        print(-1)
        return

main()
