import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    a,b,c=mi()
    a,b = b,a
    a,c = c,a

    print(a,b,c)



if __name__ == "__main__":
    main()