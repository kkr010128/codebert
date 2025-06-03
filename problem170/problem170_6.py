n,k = map(int,input().split());
kk = n-k+2
a = [0]*kk

for i in range(kk):
    ii = i + k
    p = ii*(ii-1);
    q = ii*(2*n+1-ii);
    a[i] = (q//2)-(p//2)+1;
con = 0;
for v in range(kk):
    con = (con+a[v]) % 1000000007;
    
print(con);