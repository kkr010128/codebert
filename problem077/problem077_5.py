def main():
    lis = list(map(int, input().split()))
    ans = lis[0] * lis[2]
    a, b = lis[0:2], lis[2:4]
    for i in a:
        for j in b:
            if i * j > ans:
                ans = i * j
                
    print(ans)
    
    
if __name__ == '__main__':
    main()