a,v,b,w,t=map(int,open(0).read().split())
print('YNEOS'[abs(b-a)>(v-w)*t::2])