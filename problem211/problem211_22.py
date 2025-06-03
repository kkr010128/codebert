from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n,r=map(int,readline().split())
    if n>=10:
        print(r)
    else:
        print(r+100*(10-n))
        
if __name__=="__main__":
    main()