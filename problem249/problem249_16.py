a,b,k=map(int,input().split())
print(a-k,b) if k-a<=0 else print(0,b-(k-a)) if b-(k-a)>=0 else print(0,0)