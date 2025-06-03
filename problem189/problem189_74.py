from scipy.special import comb
m,n = map(int,input().split())
print(int(comb(m,2)+comb(n,2)))