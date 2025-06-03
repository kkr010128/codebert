def main():
    n = int(input())
    S = list(map(int, input().split()))
    
    q = int(input())
    T = list(map(int, input().split()))
    
    res = 0
    for i in T:
        if i in S:
            res += 1
    print(res)
    

if __name__ == '__main__':
    main()
    
