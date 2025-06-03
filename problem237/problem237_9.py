M,a=-float("inf"),0
for X,L in sorted(zip(*[iter(map(int,open(0).read().split()[1:]))]*2),key=sum):
 l,r=X-L,X+L
 if M<=l:a+=1;M=r
print(a)