n,*d = map(int,open(0).read().split())
print(sum((sum(d)-i)*i for i in d)//2)
