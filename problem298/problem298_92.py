n,k=map(int,input().split())
h=[int(i) for i in input().split()]
h=[i for i in h if i>=k]
print(len(h))