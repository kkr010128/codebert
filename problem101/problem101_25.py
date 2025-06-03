a,b,c,k=map(int,open(0).read().split())
#while k:k-=1;t=a<b;b*=2-t;c*=1+t
while k:k-=1;exec(f'{"bc"[a<b]}*=2')
#while k:k-=1;exec('%c*=2'%'bc'[a<b])
#while k:k-=1;vars()['bc'[a<b]]*=2
print('NYoe s'[b<c::2])