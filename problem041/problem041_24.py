def main():
    W,H,x,y,r=map(int,input().split())
    if x<=0 or y<=0:
        print('No')
    elif W>=2*r and H>=2*r and W>=x+r and H>=y+r:
        print('Yes')
    else:
        print('No')

if __name__=='__main__':
    main()

