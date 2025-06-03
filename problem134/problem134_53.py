def main():
    N = int(input())
    A = list(map(int,input().split()));
    
    if 0 in A:
        print(0)
        return
    
    prod = 1
    
    for a in A:
        prod *= a
        
        if prod > 10**18:
            print(-1)
            return
        
    print(prod)

main()