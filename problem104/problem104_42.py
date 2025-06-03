def main():
    L, R, d = map(int,input().split())

    if L%d==0 and R%d==0:
        print(int((R-L)/d) + 1)
        return
    else:
        l = L - L % d
        r = R - R % d
        print(int((r - l)/d))
        return
    
if __name__=='__main__':
    main()
