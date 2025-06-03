n,k=map(int,input().split())
h=list(map(int,input().split()))
h.append(k)
print(len(h[sorted(h).index(k)+1:]))