def main():
    N = int(input())
    ans = 0

    if N == 2:
        print(2)
        return
    
    while True:
        flg = True
        for i in range(2, ((N + 1) // 2) + 1):
            if N % i == 0:
                flg = False
                break
        
        if flg:
            break
        else:
            N += 1
    
    print(N)

if __name__ == '__main__':
    main()