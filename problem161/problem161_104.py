import sys
def main():
    A,B,N=tuple(map(int,sys.stdin.readline().split()))
    L=max([1,min([B-1,N])])
    print((A*L)//B) if B!=1 else print(0)
if __name__=='__main__':main()