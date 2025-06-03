N,K = map(int,input().split())
ls = list(map(int,input().split()))
ls.sort(reverse=True)
if N <= K:
    print(0)
else:    
    print(sum(ls[K:N+1]))
