from sys import stdin
def main():
    #入力
    readline=stdin.readline
    A,B=map(int,readline().split())

    C=max(0,A-B*2)
    print(C)
if __name__=="__main__":
    main()