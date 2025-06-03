import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
def MIIZ(): return list(map(lambda x: x-1, MII()))
#======================================================#
def main():
    k = II()
    sevens = 7%k
    for i in range(1, k+1):
        if sevens % k == 0:
            print(i)
            return
        sevens = (10*sevens + 7)%k
    print(-1)

if __name__ == '__main__':
    main()