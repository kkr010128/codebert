import sys
def input(): return sys.stdin.readline().rstrip()
def main():
    k = int(input())
    keta = 1
    mod = 7%k
    while keta < 10**7:
        if mod==0:
            print(keta)
            break
        keta += 1
        mod = (mod*10 + 7)%k
    else:
        print(-1)


if __name__=='__main__':
    main()