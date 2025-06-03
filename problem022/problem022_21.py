def main():
    import sys
    asa =  sys.stdin.readline
    n = int(input())
    s = list(map(int, asa().split()))
    q = int(input())
    t = list(map(int, asa().split()))
    
    c = 0
    s.append(0)
    
    for i in t: # tの中のiを探索
        j = 0
        s[n] = i
        while s[j] != i:
            j += 1
        if j < n:
            c += 1
            
    print(c)
        
    
if __name__ == '__main__':
    main()
