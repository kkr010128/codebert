def main():
    S, W = list(map(int, input().split()))
    
    print("unsafe" if S <= W else "safe")
    pass

if __name__ == '__main__':
    main()