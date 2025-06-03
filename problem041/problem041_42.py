def main():
    W,H,x,y,r=map(int,input().split())
    if x-r>=0 and y-r>=0 and W>=x+r and H>=y+r:
        print('Yes')
    else:
        print('No')

if __name__=='__main__':
    main()
