def linearSearch(S,t):
    L = S + [t]
    i = 0
    while L[i] != t: i += 1
    if i == len(L)-1: return 0
    else            : return 1

if __name__=='__main__':
    n=input() 
    S=input().split()
    q=input() 
    T=input().split()
    cnt = 0
    for t in T: cnt += linearSearch(S,t)
    print(cnt)