def main():
    A, B = map(int,input().split())
    print( A * B if (A // 10 == 0) & (B // 10 == 0) else -1) 
    return 0
    
if __name__ == '__main__':
    main()