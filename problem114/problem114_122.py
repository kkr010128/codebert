def main():
    D = int(input())
    c = list(map(int,input().split()))
    s = []
    for d in range(D):
        s.append(list(map(int,input().split())))
        
    t = []
    for d in range(D):
        t.append(int(input())-1)
    
    last = [0 for i in range(26)]
    
    v = 0
    
    for d in range(D):
        v += s[d][t[d]]
        last[t[d]] = d+1
        for i in range(26):
            v -= c[i]*(d+1-last[i])
        print(v)
    
if __name__ == '__main__':
    main()