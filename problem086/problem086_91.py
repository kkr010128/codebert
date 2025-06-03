from math import ceil
def main():
    n,x,t=map(int,input().split())
    print(ceil(n/x)*t)
main()