a,v,b,w,t=map(int,open(0).read().split())
print('YNEOS'[v-w<abs(a-b)/t::2])