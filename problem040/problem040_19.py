def main():
    num=map(int,input().split())
    print(" ".join([str(x) for x in sorted(num)]))

if __name__=='__main__':
    main()
